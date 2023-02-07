from os import path
from os import makedirs


SRC_PATH = path.dirname(__file__)
PROJECT_PATH = path.join(SRC_PATH, "..")
BIN_PATH = path.join(PROJECT_PATH, "bin")
STORE_PATH = path.join(PROJECT_PATH, "store")

CHROME_BINARY = path.join(BIN_PATH, "chromedriver.exe")


if not path.exists(STORE_PATH):
    makedirs(STORE_PATH)
