def file_opener():
    with open('mi.txt') as f:
        return f.readlines()


def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if count_indent == 26:
            print('C|', i)
        elif count_indent == 16:
            print('D|', i)
        else:
            print(' |', i)


if __name__ == '__main__':
    count_whitespace1()

