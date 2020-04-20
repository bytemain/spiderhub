from flask import Response
from flask import request
from typing import List
import json


def filter_all(_filter: List, items: List):
    filter_list = _filter.split('|')

    new_data = []
    for i in filter_list:
        _ = list(
            filter(lambda x: i in x['title'] or i in x['description'], items))
        new_data.extend(_)
    return new_data


def filter_title(_filter: List, items: List):
    filter_list = _filter.split('|')

    new_data = []
    for i in filter_list:
        _ = list(filter(lambda x: i in x['title'], items))
        new_data.extend(_)
    return new_data


def filter_description(_filter: List, items: List):
    filter_list = _filter.split('|')

    new_data = []
    for i in filter_list:
        _ = list(filter(lambda x: i in x['description'], items))
        new_data.extend(_)
    return new_data


def args(response: Response):
    data = response.get_json()
    if data:
        items = data['items'].copy()
        _filter: str = request.args.get('filter')
        _filter_title: str = request.args.get('filter_title')
        _filter_description: str = request.args.get('filter_description')
        limit: int = request.args.get('limit', type=int)

        if _filter:
            items.extend(filter_all(_filter, items))

        if _filter_title:
            items.extend(filter_title(_filter_title, items))

        if _filter_description:
            items.extend(filter_description(_filter_description, items))

        if limit:
            items = items[:limit]

        data['items'] = items
        response.data = json.dumps(data)

    return response
