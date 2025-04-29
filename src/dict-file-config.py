import json
import logging.config
import pathlib
import json_log_formatter

logger = logging.getLogger("my_app") # use My own logger

def setup_logging():
    config_file = pathlib.Path("log_config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)
    handler = logging.StreamHandler()
    formatter = json_log_formatter.JSONFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def main():
    setup_logging()
    # logging.info("some mesage") avoid to use it
    logger.debug("This is a debug message", extra={"extra": "field"})
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("Exception message")

if __name__ == "__main__":
    main()
