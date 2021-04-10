import re
from nltk.tokenize import RegexpTokenizer

def file_opener():
    with open('mi.txt') as f:
        return f.readlines()

def count_whitespace1():
    """Counts the whitespaces of every line in a text file."""
    string = file_opener()
    metadata = ['CUT TO:', 'DISSOLVE:', 'CUT TO BLACK', 'THE END']
    tokenizer = RegexpTokenizer(r'\w+')

    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if i.strip() in metadata:
            print('M|', i)
        elif count_indent >= 26:
            print('C|', i)
        elif count_indent >= 16 and count_indent < 26 :
            print('D|', i)
        elif count_indent > 3 and count_indent < 16 and bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
            print('S|', i)
        elif count_indent > 3 and count_indent < 16 and not bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
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