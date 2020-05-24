def convert_to_python_list(short_list):
    """convert a string of shortened list into python list"""

    short_list = short_list[1:-1].split(',')      # no need of the '[' and ']'
    py_list = []

    for i in short_list:
        if '-' in i:
            start, end = i.split('-')
            start = int(start.strip())   # remove surrounding whitespaces
            end = int(end.strip())       # remove surrounding whitespaces

            py_list.extend(range(start, end + 1))

        else:
            i = int(i.strip())
            py_list.append(i)

    return py_list


if __name__ == "__main__":
    page_list = input("Enter page list: ")
    py_list = convert_to_python_list(page_list)

    missing_pages = set(range(1, 26)) - set(py_list)
    print("Missing pages are:", list(missing_pages))
