# coding:UTF-8


from quick.web import WebHandler, HttpServer, QuickApplication


class T(WebHandler):
    def get(self):
        return {"a": '测试'}

    def post(self):
        return '123'


app = QuickApplication()
app.add_route([('/', T)])

server = HttpServer()
server.start_server(app)
