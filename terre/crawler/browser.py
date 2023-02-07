from json import dumps
from typing import Optional
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Browser:
    def __init__(self, binary_file: str):
        self.service = Service(binary_file)
        self.options = Options()
        self.options.add_argument("log-level=2")
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(r"user-data-dir=C:\Users\pc\Documents\SeleniumData")
        self.driver: Optional[Chrome] = None

    def base(self):
        return self.browser

    def printer(self, output: str):
        settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
            "isHeaderFooterEnabled": False,
            "mediaSize": {
                "height_microns": 297000,
                "name": "ISO_A4",
                "width_microns": 210000,
                "custom_display_name": "A4"
            },
            "customMargins": {},
            "marginsType": 2,
            "isCssBackgroundEnabled": True
        }

        prefs = {
            'printing.print_preview_sticky_settings.appState': dumps(settings),
            'savefile.default_directory': output
        }

        self.options.add_experimental_option('prefs', prefs)
        self.options.add_argument('--kiosk-printing')
        return self.browser

    @property
    def browser(self):
        if self.driver:
            self.driver.quit()

        self.driver = Chrome(service=self.service, options=self.options)
        return self.driver
