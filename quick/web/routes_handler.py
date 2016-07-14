# coding:UTF-8


"""
路由处理模块
@author: yubang
"""


from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException


class QuickApplication(object):

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

    def __call__(self, environ, start_response):
        request = Request(environ)
        urls = self.url_map.bind_to_environ(environ)
        try:
            HandlerObject, args = urls.match()
            handler = HandlerObject(args)
            response = handler(request)
        except HTTPException:
            response = Response("not found!", status=404)
        return response(environ, start_response)
