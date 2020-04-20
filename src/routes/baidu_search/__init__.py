import requests

from bs4 import BeautifulSoup
from src.utils.result import result, item
from src.utils.utils import meta_redirect


def parse_redir_host(baidu_host):
    url = baidu_host.replace(r"^http:", "https:")
    if "eqid" not in baidu_host:
        url = url + "&wd=&eqid="

    headers = {"Accept": "*/*", "Referer": url}

    res = requests.get(url, allow_redirects=False, headers=headers)
    return meta_redirect(res.text)


def parse_content(item: BeautifulSoup):
    # class 有好几种
    # ['result-op', 'c-container', 'xpath-log']
    # ['result', 'c-container']
    # ['result-op', 'c-container']

    if 'xpath-log' in item['class']:
        title = item.select_one('h3.t > a').get_text().strip()
        desp = str(item.select_one("div.c-row"))
        link = item['mu']
    elif 'result-op' in item['class']:
        title = item.select_one('h3.t > a').get_text().strip()
        if title == '':
            item = item.div
            title = item.select_one('h3.t > a').get_text().strip()
        desp = str(item.select_one("div.c-row"))
        link = item.select_one('h3.t > a')['href']
    else:
        title = item.select_one('h3.t > a').get_text().strip()
        desp = item.select_one("div.c-abstract").get_text().strip()
        link = item.select_one('h3.t > a')['href']

    if link.startswith('http://www.baidu.com/link?url='):
        _, true_link = parse_redir_host(link)
        link = true_link if _ is True else link

    return title, desp, link


def ctx(q, number=10):
    pn = 0
    target = f"http://www.baidu.com/s?wd={q}"

    n_target = target + f"&rn={number}&pm={pn}&ie=utf-8"
    req = requests.get(n_target)
    soup = BeautifulSoup(req.text, 'lxml')
    item_list = []
    content = soup.select_one("div#content_left")
    print(len(content.select("div.c-container")))
    for _soup in content.select("div.c-container"):
        title, desp, link = parse_content(_soup)
        item_list.append(item(title=title, description=desp, link=link))

    _title = soup.select_one('title').string
    return result(title=_title, link=target, items=item_list)
