# coding:UTF-8

from BaseMiddleware import BaseMiddleware


class VersionMiddle(BaseMiddleware):
    """
    版本号中间件
    """

    def __init__(self, config):
        super(VersionMiddle, self).__init__(config)
        self.version = "version: 1.0(beta), 20160714"

    def before_request(self, request):
        pass

    def after_request(self, request, response):
        response.headers['server'] = self.version
        return response
