import config
import pprint
import logging

logger = logging.getLogger(__name__)

app = config.get_app_singletone(__name__)
logger.info("import flask_tutorial")

import flask_tutorial


@app.route('/help')
def url_map():
    return "<pre>" + str(pprint.pformat(app.url_map, indent=4)) + "</pre>"


if __name__ == "__main__":
    logger.info(f'if {__name__} == "__main__":')
    logger.info(app.url_map)
    logger.info(f"app.run(host={config.HOST_IP}, debug=True)")
    app.run(host=config.HOST_IP, debug=True)
    logger.info("-" * 80)
