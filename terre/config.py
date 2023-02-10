from os import path
from os import makedirs


def ensure_path(filepath: str) -> str:
    if not path.exists(filepath):
        makedirs(filepath)
    return filepath


PROJECT_PATH = path.join(path.dirname(__file__), "..")

LOGS_PATH = path.join(PROJECT_PATH, "logs")
BIN_PATH = path.join(PROJECT_PATH, "bin")
STORE_PATH = path.join(PROJECT_PATH, "store")

CHROME_BINARY = path.join(BIN_PATH, "chromedriver.exe")

ensure_path(LOGS_PATH)
ensure_path(STORE_PATH)
ensure_path(BIN_PATH)
