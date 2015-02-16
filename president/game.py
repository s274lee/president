'''
Created on Feb 15, 2015

@author: all
'''
import os
from flask import Flask #For routing
from jinja2 import Environment, PackageLoader #For templating
from tornado import websocket

#Initialize components
app = Flask(__name__) 
env = Environment(loader=PackageLoader('game', 'templates'))

#Open websocket
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

#Home page route
@app.route('/')
def hello_world():
    template = env.get_template('mytemplate.html')
    return template.render(var='var')

@app.route('/websocket')
def test_websocket():
    socket = EchoWebSocket()
    return socket

#Run the web application on port 5000
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)