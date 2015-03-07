'''
Created on Feb 16, 2015

@author: Rebecca
'''
import os
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.ioloop import IOLoop
from websocket import WSHandler
from flask_sockets import Sockets
from jinja2 import Environment, FileSystemLoader #PackageLoader #For templating

#import views
#from president import app

if __name__ == '__main__':
    
    from flask import Flask
    
    app = Flask(__name__)
	sockets = Sockets(app)
	
    app.secret_key = os.urandom(24)
    app.debug = True
    
    env = Environment(
    loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__))
    )
    
    port = int(os.environ.get('PORT', 5000))

    #Home page route
    @app.route('/')
    def hello_world():
        template = env.get_template('waiting_room.html')
        return template.render()
    
	
    #Check the websocket port
    @app.route('/port')
    def print_port():
        print (port)
    
    wsgi_app = WSGIContainer(app)
    
    application = Application([
        (r'/websocket', WSHandler),
        (r'.*', FallbackHandler, dict(fallback=wsgi_app))
    ])

    application.listen(6543)
    IOLoop.instance().start()

    app.run(host='prezzy.herokuapp.com', port=5000)