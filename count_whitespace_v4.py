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

    all_text_list = []
    dialogue_list = []

    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if i.strip() in metadata:
            all_text_list += ['M|', i]
            # print('M|', i)
        elif count_indent >= 26:
            all_text_list += ['C|', i]
            # print('C|', i)
        elif 16 <= count_indent < 26 and not i.strip().startswith('('):
            dialogue_list += [['D|', i.strip()]]
            all_text_list += ['D|', i]
            # print('D|', i)
        elif 3 < count_indent < 16 and bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
            all_text_list += ['S|', i]
            # print('S|', i)
        elif 3 < count_indent < 16 and not bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
            all_text_list += ['N|', i]
            # print('N|', i)
        elif i.strip().startswith('(') and i.strip().endswith(')'):
            all_text_list += ['M|', i]
            # print('M|', i)
        else:
            all_text_list += [' |', i]
            # print(' |', i)

    return ''.join(all_text_list)


# def count_whitespace():
#     """Counts the whitespaces of every line in a text file."""
#     string = file_opener()
#     for i in string:
#         count_indent = len(i) - len(i.lstrip())
#         print(count_indent, i)


def main():
    print(count_whitespace1())


if __name__ == '__main__':
    main()
