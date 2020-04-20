from bs4 import BeautifulSoup


def meta_redirect(content):
    soup = BeautifulSoup(content, 'lxml')

    result = soup.find("meta", attrs={"http-equiv": "refresh"})
    if result:
        wait, text = result["content"].split(";")
        text = text.strip()
        if text.lower().startswith("url="):
            url = text[4:]
            return True, url
    return False, None
