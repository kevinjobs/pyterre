from os import path
from os import makedirs


PROJECT_PATH = path.join(path.dirname(__file__), "..")
BIN_PATH = path.join(PROJECT_PATH, "bin")
STORE_PATH = path.join(PROJECT_PATH, "store")

CHROME_BINARY = path.join(BIN_PATH, "chromedriver.exe")


if not path.exists(STORE_PATH):
    makedirs(STORE_PATH)
