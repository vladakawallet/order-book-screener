import logging 
from logging.handlers import RotatingFileHandler
import os

class LevelFilter(logging.Filter):
    def __init__(self, levels):
        super().__init__()
        self.levels = set(levels)

    def filter(self, record):
        return record.levelno in self.levels


def setup_logger(name: str, path: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    os.makedirs(os.path.join(path, "logs"), exist_ok=True)

    formatter = logging.Formatter("%(asctime)s - %(name)s - [%(levelname)s]: %(message)s")

    # Info logs
    info_handler = RotatingFileHandler(
        filename=os.path.join(path, "logs", f"{name}.out.log"),
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
    )
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(LevelFilter([logging.INFO, logging.DEBUG]))
    info_handler.setFormatter(formatter)

    # Error logs
    error_handler = RotatingFileHandler(
        filename=os.path.join(path, "logs", f"{name}.err.log"),
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
    )
    error_handler.setLevel(logging.WARNING)
    error_handler.addFilter(LevelFilter([logging.ERROR, logging.CRITICAL, logging.WARNING]))
    error_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger