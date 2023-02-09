import requests
from bs4 import BeautifulSoup
from terre.ramper import Ramper
from terre.ramper import RamperItem
from terre.ramper import StringField


class IthomeItem(RamperItem):
    title = StringField()
    link = StringField()


class IthomeRamper(Ramper):
    def __init__(self):
        super().__init__()

    def parse(self):
        base_url = "https://www.ithome.com/"
        page_url = base_url
        resp = requests.get(page_url)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        list_container = soup.find("ul", class_="bd order sel")
        items = list_container.find_all("li")

        for item in items:
            my_item = IthomeItem()
            a = item.find("a")

            my_item.title = a.get_text()
            my_item.link = a.attrs.get("href")
            yield my_item
