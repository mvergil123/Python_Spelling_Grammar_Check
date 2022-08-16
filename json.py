import json


def parse_content_into_arr():
    f = open("content.json", "r")
    str = f.read()
    arr = json.loads(str).decode("utf-8")
    return arr














