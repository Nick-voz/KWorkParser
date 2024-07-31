import logging

from logger_conf import loger_config

loger_config()
logger = logging.getLogger(__name__)
try:
    tmp = 1 / 0
except ZeroDivisionError as e:
    logger.error("do not do that", exc_info=e)
