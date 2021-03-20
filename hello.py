from flask import Flask
import config

app = Flask(__name__)
print(__name__)

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


if __name__ == "__main__":
    app.run(host=config.HOST_IP, debug=True)
