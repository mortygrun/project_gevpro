import re


def file_opener():
    with open('testchar.txt') as f:
        return f.readlines()


def compile_regex():
    digits = re.compile("[0-9]+")
    return digits


def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    digits = compile_regex()
    metadata = ['CUT TO:', 'DISSOLVE:', 'CUT TO BLACK', 'THE END']
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if i.strip() in metadata:
            print('M|', i)
        elif count_indent >= 26 and not re.search(digits, i):  # all capitalized
            print('C|', i)
        elif 16 <= count_indent < 26:  # normal
            print('D|', i)
        elif 3 < count_indent < 16 and i.isupper():  # all capitalized
            print('S|', i)
        elif 3 < count_indent < 16 and not i.isupper():  # normal
            print('N|', i)
        elif i.strip().startswith('(') and i.strip().endswith(')'):
            print('M|', i)
        else:
            print(' |', i)


def count_whitespace():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        print(count_indent, i)


if __name__ == '__main__':
    count_whitespace1()
