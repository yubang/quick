# coding:UTF-8


"""
内置中间件模块
@author: yubang
"""

import time

from quick.middleware import BaseMiddler


class QuickVersionMiddler(BaseMiddler):
    """
    版本号中间件
    """

    def __init__(self, config):
        super(QuickVersionMiddler, self).__init__(config)
        self.version = "version: 1.0(beta), 20160714"

    def before_request(self, request):
        pass

    def after_request(self, request, response):
        response.headers['server'] = self.version
        return response


class QuickRequestTimeMiddler(BaseMiddler):
    def __init__(self, config):
        super(QuickRequestTimeMiddler, self).__init__(config)
        self.start_time = time.time()

    def before_request(self, request):
        pass

    def after_request(self, request, response):
        use_time = time.time() - self.start_time
        response.headers['use_time'] = str(use_time)
        return response
