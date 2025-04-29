import logging

logger = logging.getLogger("my_app")

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("This is a debug message")
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
