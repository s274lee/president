'''
Created on Feb 15, 2015

@author: all
'''
'''
import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True

from president import views
'''

