# coding:UTF-8


from quick.middleware import VersionMiddle, RequestTimeMiddleware, SessionMiddleware
from quick.web import WebHandler, HttpServer, QuickApplication


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
app.add_middleware([VersionMiddle, RequestTimeMiddleware])
app.add_middleware([SessionMiddleware])

server = HttpServer()
server.start_server(app)
