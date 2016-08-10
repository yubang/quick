# coding:UTF-8


"""
路由处理模块
@author: yubang
"""

from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response


class QuickApplication(object):
    config = {}

    def __build_route(self):
        """
        刷新路由规则
        :return:
        """
        routes = []
        for obj in self.routes:
            routes.append(Rule(obj[0], endpoint=obj[1]))
        self.url_map = Map(routes)

    def __init__(self, app_name="default"):
        self.routes = []
        self.middleware = []
        self.app_name = app_name
        self.__build_route()

    def add_route(self, routes):
        """
        添加路由规则
        :param routes: 路由列表[(url规则，处理类),(url规则，处理类)]
        :return:
        """
        self.routes += routes
        self.__build_route()

    def add_middleware(self, middleware):
        """
        添加中间件
        :param middleware: [中间件, ]
        :return:
        """
        self.middleware += middleware

    @staticmethod
    def __before_request(request, middle_objs):
        """
        在请求前调用
        :return:
        """
        for obj in middle_objs:
            if not hasattr(obj, "before_request"):
                continue
            r = obj.before_request(request)
            if r:
                return r

    @staticmethod
    def __after_request(request, response, middle_objs):
        """
        在请求后处理
        :param request:
        :param response:
        :param middle_objs:
        :return:
        """
        middle_objs.reverse()
        for obj in middle_objs:
            if not hasattr(obj, "after_request"):
                continue
            response = obj.after_request(request, response)
        return response

    def __call__(self, environ, start_response):
        request = Request(environ)

        # 中间件前置处理
        middle_objs = map(lambda x: x(self.config), self.middleware)
        self.__before_request(request, middle_objs)

        urls = self.url_map.bind_to_environ(environ)
        try:
            HandlerObject, args = urls.match()
            handler = HandlerObject(args)
            response = handler(request)
            response = self.__after_request(request, response, middle_objs)
        except HTTPException:
            response = Response("not found!", status=404)

        return response(environ, start_response)
