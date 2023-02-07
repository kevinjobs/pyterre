from selenium.webdriver import Chrome
from usine.crawler.browser import Browser
from usine.config import CHROME_BINARY
from usine.config import STORE_PATH


def test_browser():
    browser = Browser(CHROME_BINARY)
    base = browser.base()
    printer = browser.printer(STORE_PATH)
    assert isinstance(base, Chrome)
    assert isinstance(printer, Chrome)
