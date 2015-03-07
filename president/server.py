'''
Created on Feb 16, 2015

@author: Rebecca
'''
import os
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.ioloop import IOLoop
from websocket import WSHandler
from jinja2 import Environment, FileSystemLoader #PackageLoader #For templating

#import views
#from president import app

if __name__ == '__main__':
    
    from flask import Flask
    
    app = Flask(__name__)

    app.secret_key = os.urandom(24)
    app.debug = True
    
    env = Environment(
    loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
    
    port = int(os.environ.get('PORT', 5000))
    
    wsgi_app = WSGIContainer(app)
    
    application = Application([
        (r'/websocket', WSHandler),
        (r'.*', FallbackHandler, dict(fallback=wsgi_app))
    ])

    #Home page route
    @app.route('/')
    def hello_world():
        # write the port variable to the file myport.txt
        f = open('myport.txt', 'w')
        f.write(str(port))
        template = env.get_template('waiting_room.html')
        return template.render(port=port)
    
    #Check the websocket port
    @app.route('/print/port')
    def print_port():
        template = env.get_template('mytemplate.html')
        return template.render(port=port)

    application.listen(port)
    IOLoop.instance().start()

    app.run(host='prezzy.herokuapp.com', port=port)
