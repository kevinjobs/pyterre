from os import path
import time
from terre.web.util.render_static import render_static
from terre.config import STORE_PATH
from terre.util.day import now_stamp
from rampers.hupu import HupuRamper


def task():
    tpl = '''
    <ul>
    {% for item in data %}
    <li><a href="{{ item.link }}">{{ item.title }}</a></li>
    {% endfor %}
    </ul>
    '''
    data = HupuRamper().to_json()
    html = render_static(tpl, data=data)
    filepath = path.join(STORE_PATH, f"index.html")  # hupu-{now_stamp()}.html
    print("gen new: ", filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    while True:
        task()
        time.sleep(600)
