import logging

class Logger:

    logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
            format="%(name)s - %(levelname)s - %(message)s")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(console_handler)

    @staticmethod
    def info(message="You have been informed"):
        Logger.logger.info(message);

    @staticmethod
    def warning(message="You have been warned"):
        Logger.logger.info(message)

    @staticmethod
    def error(message="An error has occurred"):
        Logger.logger.info(message)


if __name__ == "__main__":
    Logger.info("Info")
    Logger.warning("Warning")
    Logger.error("Error")
