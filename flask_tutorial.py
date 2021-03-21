import config
import logging

logger = logging.getLogger(__name__)
# logger.info(" from hello import app")
# from hello import app
app = config.get_app_singletone(__name__)
logger.info("     START route definitions")


def bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def em(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


# http://192.168.1.10:5000/
@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">hello, world!</h1>' \
           '<p>helloooooooooooooooo</p>' \
           '<img width="200" src="https://media1.tenor.com/images/a52c4d90765b8a123712cdb6164e79f7/tenor.gif?itemid=17800101">'


# http://192.168.1.10:5000/bye
@app.route('/bye')
@bold
@em
@underline
def bye():
    return "bye!"


# http://192.168.1.10:5000/{name}
@app.route('/<name>')
def username(name):
    return f"hello {name}"


# http://192.168.1.10:5000/username/{name}
@app.route('/username/<name>')
def greet(name):
    return f"hello {name}"


# http://192.168.1.10:5000/path/{some/words/separated/by/slash}
@app.route('/path/<path:path>')
def get_path(path):
    return path


# http://192.168.1.10:5000/variables/{name}/{any number}
@app.route('/variables/<name>/<int:number>')
def variables(name, number):
    return f"{name}, {number}"


logger.info("     END route definitions")
