'''
Created on Feb 15, 2015

@author: all
'''
from flask import Flask
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('game', 'templates'))

@app.route('/')
def hello_world():
    template = env.get_template('mytemplate.html')
    return template.render(var='var')

if __name__ == '__main__':
    app.run()