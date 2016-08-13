# coding:UTF-8

"""
核心响应类封装
@author: yubang
"""

from werkzeug.wrappers import Request, Response
import datetime
import json


class WebHandler(object):
    def __init__(self, args):
        self.__args = args

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass

    def head(self):
        pass

    def options(self):
        pass

    def unknown_http_method(self):
        pass

    def __handle_request(self, request):
        """
        分配方法处理请求
        :return:
        """
        self.request = request

        if self.request.method == 'GET':
            result = self.get()
        elif self.request.method == 'POST':
            result = self.post()
        elif self.request.method == 'DELETE':
            result = self.delete()
        elif self.request.method == 'PUT':
            result = self.put()
        elif self.request.method == 'PATCH':
            result = self.patch()
        elif self.request.method == 'HEAD':
            result = self.head()
        elif self.request.method == 'OPTIONS':
            result = self.options()
        else:
            result = self.unknown_http_method()

        response = self.__make_quick_response(result)

        return response

    def __make_quick_response(self, result):
        """
        制作响应对象
        :param result:  输出内容
        :return:
        """
        if result is None:
            return Response("Method not allowed", 405)
        if isinstance(result, (list, dict)):
            return Response(json.dumps(result), 200, mimetype="application/json")
        if isinstance(result, (str, unicode)):
            return Response(result, 200)
        if isinstance(result, (int, float, bool)):
            return Response(str(result), 200)
        if isinstance(result, datetime.datetime):
            return Response(result.strftime("%Y-%m-%d %H:%M:%S"), 200)
        if isinstance(result, datetime.date):
            return Response(result.strftime("%Y-%m-%d"), 200)
        return Response(result, 200)

    def __call__(self, request):
        """
        入口方法
        :return:
        """
        return self.__handle_request(request)
