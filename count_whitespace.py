def file_opener():
    with open('mi.txt') as f:
        return f.readlines()


def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        print(count_indent, i)


if __name__ == '__main__':
    count_whitespace1()

