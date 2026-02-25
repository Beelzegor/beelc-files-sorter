import logging
from pathlib import Path

def setup_logger(name: str = "file_sorter") -> logging.Logger:
    log_folder = Path("logs")
    log_folder.mkdir(exist_ok=True)

    log_file = log_folder / "app.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)


    if logger.handlers:
        return logger


    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)


    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger