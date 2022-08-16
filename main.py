from content import content_as_array
from spelling import check_list_for_spelling


def main():
    content_arr = content_as_array()

    try:
        check_list_for_spelling(content_arr)
    except Exception as e:
        err_message = str(e)
        print(err_message)
        quit(1)








if __name__ == "__main__":
    main()


