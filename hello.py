import config
import pprint

app = config.get_app_singletone(__name__)
print("import flask_tutorial")

import flask_tutorial


@app.route('/help')
def url_map():
    return "<pre>" + str(pprint.pformat(app.url_map, indent=4)) + "</pre>"


if __name__ == "__main__":
    print(f'if {__name__} == "__main__":')
    print(app.url_map)
    print(f"app.run(host={config.HOST_IP}, debug=True)")
    app.run(host=config.HOST_IP, debug=True)
    print("-" * 80)
