from flask import jsonify
import arrow


def result(title, link, items, description=None):
    update_time = arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ')
    total = len(items)
    return jsonify(title=title,
                   link=link,
                   description=description,
                   items=items,
                   total=total,
                   updated=update_time)


def item(title, link, description, update_time=None, guid=None):
    if guid is None:
        guid = link

    return {
        "title": title,
        "link": link,
        "guid": guid,
        "description": description,
        "updateTime": update_time,
    }
