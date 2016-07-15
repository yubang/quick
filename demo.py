# coding:UTF-8


from quick.web import WebHandler, HttpServer, QuickApplication
from quick.tools.middler import QuickVersionMiddler, QuickRequestTimeMiddler
from quick.middler.session_middler import CookieSessionMiddler


class T(WebHandler):
    def get(self):
        print self.request.session
        self.request.session['test'] = 'abc'
        return {"a": '测试'}

    def post(self):
        return '123'


app = QuickApplication()
app.config['key'] = '123456'
app.add_route([('/', T)])
app.add_middles([QuickVersionMiddler, QuickRequestTimeMiddler])
app.add_middles([CookieSessionMiddler])

server = HttpServer()
server.start_server(app)
