print(" from hello import app")
from hello import app

print("     START route definitions")


# http://192.168.1.10:5000/
@app.route('/')
def hello_world():
    return "hello, world!"


# http://192.168.1.10:5000/bye
@app.route('/bye')
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


print("     END route definitions")
