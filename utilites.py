import json
import logging.config


def config_loger():
    """load "logger_conf.json" and config logging"""
    with open("logger_conf.json", "r", encoding="utf8") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
