import logging

LOG_FORMAT = r"%(levelname)s: %(name)s: %(asctime)s: %(message)s:"
LOG_DATE_FORMAT = r"%y-%m-%d %H:%M:%S"
LOG_FILE_NAME = "app.log"
LOG_LEVEL = logging.DEBUG


def loger_config():
    # TODO: do more flexable logging
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        filename=LOG_FILE_NAME,
        filemode="a",
    )


if __name__ == "__main__":
    pass
