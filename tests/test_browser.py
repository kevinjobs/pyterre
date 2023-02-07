from selenium.webdriver import Chrome
from pyterre.crawler.browser import Browser
from pyterre.config import CHROME_BINARY
from pyterre.config import STORE_PATH


def test_browser():
    browser = Browser(CHROME_BINARY)
    base = browser.base()
    printer = browser.printer(STORE_PATH)
    assert isinstance(base, Chrome)
    assert isinstance(printer, Chrome)
