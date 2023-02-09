import requests
from bs4 import BeautifulSoup
from terre.ramper import Ramper
from terre.ramper import RamperItem
from terre.ramper import StringField


class ZhihuItem(RamperItem):
    title = StringField()
    excerpt = StringField()
    link = StringField()


class ZhihuRamper(Ramper):
    def __init__(self):
        super().__init__()

    def parse(self):
        base_url = "https://www.zhihu.com"
        page_url = base_url + "/billboard"
        resp = requests.get(page_url)
        soup = BeautifulSoup(resp.text, "html.parser")
        list_container = soup.find("div", class_="Card")
        items = list_container.find_all("a", class_="HotList-item")

        for item in items:
            my_item = ZhihuItem()
            body = item.find("div", class_="HotList-itemBody")
            item_title = body.find("div", class_="HotList-itemTitle")
            item_excerpt = body.find("div", class_="HotList-itemExcerpt")
            my_item.title = item_title.get_text()
            my_item.excerpt = item_excerpt.get_text()
            yield my_item
