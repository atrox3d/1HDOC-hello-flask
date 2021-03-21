import logging
import sys
from flask import Flask


def get_rootlogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    levelname = logging.getLevelName(logger.getEffectiveLevel())
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)-40s | %(message)s'))
    logger.addHandler(handler)
    logger.info(f"Created root logger in module {__name__} with level {levelname}")
    return logger


rootlogger: logging.Logger = get_rootlogger()

HOST_IP = "192.168.1.10"
rootlogger.info(f"HOST_IP = {HOST_IP}")

_app = None


def get_app_singletone(name) -> Flask:
    global _app
    rootlogger.info(f"get_app({name})")
    rootlogger.info(f"app = {_app}")
    if not _app:
        rootlogger.info(f"app = Flask({name})")
        _app = Flask(name)
    rootlogger.info(f"return app {_app}")
    return _app
