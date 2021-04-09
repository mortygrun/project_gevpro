

def file_opener():
    with open('mi.txt') as f:
        return f.readlines()


def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    metadata = ['CUT TO:', 'DISSOLVE:', 'CUT TO BLACK', 'THE END']
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
        elif i.strip() in metadata:
            print('M|', i)
        elif i.strip().startswith('(') and i.strip().endswith(')'):
            print('M|', i)
        else:
            print(' |', i)


if __name__ == '__main__':
    count_whitespace1()
