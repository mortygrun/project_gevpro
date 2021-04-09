def file_opener():
    with open('mi.txt') as f:
        return f.readlines()


def create_dictionary():
    scenebound_dict = {'M|': ['CUT TO:', 'DISSOLVE TO:']}
    return scenebound_dict


def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    scenebound_dict = create_dictionary()
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if count_indent == 26:
            print('C|', i)
        elif count_indent == 16:
            print('D|', i)
        elif count_indent == 5 and i.isupper():
            print('S|', i)
        elif count_indent == 5 and not i.isupper():
            print('N|', i)
        elif i.lstrip().startswith('(') and i.rstrip().endswith(')'):
            print('M|', i)
        elif count_indent < 3:
            print(' |', i)
        for keys, values in scenebound_dict.items():
            for value in values:
                if value in i:
                    print(keys, i)


def count_whitespace():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    for i in string:
        count_indent = len(i) - len(i.lstrip())
        print(count_indent, i)


if __name__ == '__main__':
    count_whitespace1()

