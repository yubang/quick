# coding:UTF-8


"""
内置中间件模块
@author: yubang
"""

import time


class BaseMiddler(object):
    def before_request(self, request):
        pass

    def after_request(self, request, response):
        return response


class QuickVersionMiddler(BaseMiddler):
    """
    版本号中间件
    """

    def before_request(self, request):
        self.version = "version: 1.0(beta), 20160714"

    def after_request(self, request, response):
        response.headers['server'] = self.version
        return response


class QuickRequestTimeMiddler(BaseMiddler):
    def before_request(self, request):
        self.start_time = time.time()

    def after_request(self, request, response):
        self.end_time = time.time()
        use_time = self.end_time - self.start_time
        response.headers['use_time'] = str(use_time)
        return response
