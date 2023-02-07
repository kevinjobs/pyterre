import requests
from bs4 import BeautifulSoup
from terre.ramper import Ramper


class MyRamper(Ramper):
    def __init__(self):
        super().__init__()

    def start(self):
        base_url = "https://bbs.hupu.com"
        page_url = base_url + "/all-gambia"
        resp = requests.get(page_url)
        soup = BeautifulSoup(resp.text, "html.parser")
        list_container = soup.find("div", class_="text-list-model")
        items = list_container.find_all("div", class_="list-item-wrap")

        data = []
        for item in items:
            info = item.find("div", class_="t-info")
            cate = item.find("div", class_="t-label")
            if info:
                title = info.find("span", class_="t-title").get_text()
                link = base_url + info.find("a").attrs.get("href")
                data.append({"title": title, "link": link})
        return data

    def filter(self):
        pass


if __name__ == "__main__":
    mr = MyRamper()
    mr.run()
