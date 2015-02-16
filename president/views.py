from jinja2 import Environment, PackageLoader #For templating
from president import app

env = Environment(loader=PackageLoader('president', 'templates'))

#Home page routes
@app.route('/')
def hello_world():
    template = env.get_template('waiting_room.html')