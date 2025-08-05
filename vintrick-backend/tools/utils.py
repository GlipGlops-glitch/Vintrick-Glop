import os
import re
import logging

def safe_dir_name(name: str) -> str:
    """
    Sanitize a string to be safe as a directory name.
    Allows alphanumerics, dash, underscore, and dot.
    Replaces all other characters with underscore.
    """
    return re.sub(r"[^a-zA-Z0-9_.-]", "_", name)

def setup_logging(log_dir: str = "Main/Logs", log_file: str = "fetch.log", level=logging.INFO):
    """
    Sets up logging to file and stdout.
    """
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized. Log file at {log_path}")
    return logger