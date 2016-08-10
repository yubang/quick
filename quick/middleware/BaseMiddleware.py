# coding:UTF-8


"""
基础中间件
@author: yubang
"""


class BaseMiddleware(object):

    def __init__(self, config):
        self.config = config

    def before_request(self, request):
        pass

    def after_request(self, request, response):
        return response
