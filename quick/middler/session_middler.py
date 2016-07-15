# coding:UTF-8


"""
处理session的中间件
@author: yubang
"""


from quick.middler import BaseMiddler
import pickle


class CookieSessionMiddler(BaseMiddler):

    def before_request(self, request):
        try:
            c = request.cookies.get('session_id', None)
            request.session = pickle.loads(c)
        except:
            request.session = {}

    def after_request(self, request, response):
        session_string = pickle.dumps(request.session)
        response.set_cookie("session_id", session_string)
        return response

