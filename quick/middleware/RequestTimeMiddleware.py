# coding:UTF-8

import time

from BaseMiddleware import BaseMiddleware


class RequestTimeMiddleware(BaseMiddleware):
    def __init__(self, config):
        super(RequestTimeMiddleware, self).__init__(config)
        self.start_time = time.time()

    def before_request(self, request):
        pass

    def after_request(self, request, response):
        use_time = time.time() - self.start_time
        response.headers['use_time'] = str(use_time)
        return response
