from os import path
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from terre.browser import Browser
from terre.util import save_json
from terre.util import read_json
from terre.util import read_file
from terre.util.array import concat
from terre.config import CHROME_BINARY
from terre.config import STORE_PATH


def fetch_publish_lists(start=1, end=30):
    """fetch the publishing article lists
    :Args:
      - start: start page
      - end: end page
    """
    home_url = "https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN"
    browser = Browser(CHROME_BINARY).base()
    browser.set_window_size(width=1400, height=1000, windowHandle="current")
    browser.get(home_url)

    try:
        msg_content = browser.find_element(By.CLASS_NAME, "msg_content")
        h2 = msg_content.find_element(By.TAG_NAME, "h2")
        if h2.text == "请重新登录":
            re_login(browser)
    except Exception as e:
        print(e)

    goto_publish_page(browser)

    all_lists = []
    for page in range(start, end):
        lists = extract_lists(browser)
        all_lists = concat(all_lists, lists)
        goto_next_page(browser)
    save_json(path.join(STORE_PATH, "publish_list.json"), all_lists)


def extract_lists(browser: Chrome):
    data = []
    publish_content = browser.find_element(By.CLASS_NAME, "publish_content")
    post_items = publish_content \
        .find_elements(By.CLASS_NAME, "weui-desktop-block")
    for p in post_items:
        post_date = p.find_element(
            By.CLASS_NAME, "weui-desktop-mass__time").text
        post_status = p.find_element(By.CLASS_NAME, "js_status_txt").text

        posts = p.find_elements(By.CLASS_NAME, "publish_hover_content")

        for post in posts:
            post_info = post \
                .find_element(By.CLASS_NAME, "weui-desktop-mass-appmsg__title")
            post_url = post_info.get_attribute("href")
            post_title = post_info.find_elements(By.TAG_NAME, "span")[0].text

            view_counts = post \
                .find_elements(By.CLASS_NAME, "weui-desktop-tooltip__wrp")

            try:
                counts = view_counts[0].find_element(
                            By.CLASS_NAME,
                            "weui-desktop-mass-media__data__inner"
                        ).text
            except Exception as e:
                print(e)
                counts = 0

            data.append({
                "date": post_date,
                "url": post_url,
                "title": post_title,
                "status": post_status,
                "view_counts": counts
            })
    return data


def goto_publish_page(browser: Chrome):
    items = browser.find_elements(By.CLASS_NAME, "weui-desktop-sub-menu__item")
    items[3].click()
    wait_()


def goto_next_page(browser: Chrome):
    paging = browser.find_element(
        By.CLASS_NAME,
        "weui-desktop-pagination__nav"
    )
    prev_next = paging.find_elements(By.CLASS_NAME, "weui-desktop-btn_mini")
    if len(prev_next) == 1:
        prev_next[0].click()
    else:
        prev_next[1].click()
    sleep(3)


def re_login(browser: Chrome):
    jump_url = browser.find_element(By.ID, "jumpUrl")
    if jump_url:
        jump_url.click()


def trim_title(title: str):
    title.replace("\\", "")
    title.replace(r"/", "")
    title.replace(r":", "")
    title.replace(r"*", "")
    title.replace(r"?", "")
    title.replace(r'"', "")
    title.replace(r"<", "")
    title.replace(r">", "")
    title.replace(r"|", "")
    return title


def wait_():
    sleep(5)


def save_pdf():
    publist_lists = path.join(STORE_PATH, "publish_lists.json")
    scroll_js = path.join(STORE_PATH, "scroll.js")
    show_msg_js = path.join(STORE_PATH, "show_msg.js")

    lists = read_json(publist_lists)
    scroll_script = read_file(scroll_js).replace("\n", "")
    show_msg = read_file(show_msg_js).replace("\n", "")

    pdf_path = path.join(STORE_PATH, "pdf")
    browser = Browser(CHROME_BINARY).printer(pdf_path)
    for item in lists:
        url = item.get("url")
        date = item.get("date")
        title = trim_title(item.get("title"))
        file_title = date + " " + title

        pdf_path = path.join(STORE_PATH, "pdf")
        file_path = path.join(pdf_path, file_title + ".pdf")

        if not path.exists(file_path):
            print("to save: ", file_path)
            browser.get(url)

            seconds = browser.execute_script(show_msg)
            browser.execute_script(scroll_script)

            sleep(seconds)

            browser.execute_script(
                'document.title="' + file_title + '";window.print();'
            )
        else:
            print("exists: ", file_path)


if __name__ == "__main__":
    # start()
    save_pdf()
