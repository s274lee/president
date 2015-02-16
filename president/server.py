'''
Created on Feb 16, 2015

@author: Rebecca
'''

from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.ioloop import IOLoop
from president.websocket import WSHandler
from president import app

if __name__ == '__main__':
    wsgi_app = WSGIContainer(app)

    application = Application([
        (r'/websocket', WSHandler),
        (r'.*', FallbackHandler, dict(fallback=wsgi_app))
    ])

    application.listen(5000)
    IOLoop.instance().start()