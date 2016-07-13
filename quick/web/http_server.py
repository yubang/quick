# coding:UTF-8


"""
简易http服务器封装模块
@author: yubang
"""

from werkzeug.serving import run_simple


class HttpServer(object):
    def start_server(self, wsgi_app, host='127.0.0.1', port=8080, debug=True, use_reload=True):
        """
        启动一个简易的服务器
        :param wsgi_app:  wsgi接口函数
        :param host:  监听的域名
        :param port:  监听的端口
        :param debug:  是否开启调试
        :param use_reload:  是否自动加载代码
        :return:
        """
        run_simple(host, port, wsgi_app, use_reload, debug)
