from flask import Flask
import config

print(f"app = Flask({__name__})")
app = Flask(__name__)

print("import flask_tutorial")
import flask_tutorial


if __name__ == "__main__":
    print(f'if {__name__} == "__main__":')
    print("app.run(host=config.HOST_IP, debug=True)")
    app.run(host=config.HOST_IP, debug=True)
    print("-" * 80)