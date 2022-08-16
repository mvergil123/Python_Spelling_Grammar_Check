import json


def parse_content_into_arr():
    f = open("content.json", "r")
    str = f.read()
    arr = json.loads(str)
    return arr


# returns an array of words to check spelling
def convert_array_to_single_array(arr):
    single_arr = []

    for page in arr["pages"]:
        page_data = page["pageData"]
        nav_content = page_data["linkNavContent"]
        headline = page_data["headline"]
        subheadline = page_data["subHeadline"]
        content = page_data["content"]

        str = f"{nav_content} {headline} {subheadline} {content}"
        str = str.replace(",", "")
        str = str.replace(".", "")
        str = str.replace("(", "")
        str = str.replace(")", "")
        str = str.replace("'s", "")
        str = str.replace("'", "")
        str = str.replace(":", "")

        words = str.split(" ")

        for word in words:
            if len(word) > 0:
                if "-" in word:
                    dash_words = word.split("-")
                    for dash_word in dash_words:
                        dash_word = dash_word.lower()
                        single_arr.append(dash_word)
                else:
                    word = word.lower()
                    single_arr.append(word)

    return single_arr


def content_as_array():
    return convert_array_to_single_array(parse_content_into_arr())






























