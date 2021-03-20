from flask import Flask

HOST_IP = "192.168.1.10"
_app = None


def get_app_singletone(name) -> Flask:
    global _app
    print(f"get_app({name})")
    print(f"app = {_app}")
    if not _app:
        print(f"app = Flask({name})")
        _app = Flask(name)
    print("return app")
    return _app

