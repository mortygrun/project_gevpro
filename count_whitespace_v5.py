import re
from nltk.tokenize import RegexpTokenizer
import pysrt


def file_opener():
    with open('mi.txt') as f:
        return f.readlines()


def count_whitespace1():
    """Counts the whitespaces of every line in a text file and returns a list of all the dialogues"""
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
        elif 16 <= count_indent < 26 and not i.strip().startswith('(') and not i.isupper():
            dialogue_list += [' '.join(tokenizer.tokenize(i.strip()))]
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

    return dialogue_list


def dialogue():
    string = file_opener()
    tokenizer = RegexpTokenizer(r'\w+')

    dialogue_list = []

    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if 16 <= count_indent < 26 and not i.strip().startswith('(') and not i.isupper():
            dialogue_list += [' '.join(tokenizer.tokenize(i.strip()))]
    return dialogue_list

# def count_whitespace():
#     """Counts the whitespaces of every line in a text file."""
#     string = file_opener()
#     for i in string:
#         count_indent = len(i) - len(i.lstrip())
#         print(count_indent, i)


def subtitles_open():
    # You have to save the .srt file with utf-8 first
    subs = pysrt.open('mi_utf8.srt')
    return subs


def tokenize():
    """ This function returns a list of subtitles (each item is a subtitle) """
    tokenizer = RegexpTokenizer(r'\w+')
    subtitle_token = subtitles_open()
    sentence_list = []
    for i in subtitle_token:
        sentence_list += [' '.join(tokenizer.tokenize(i.text))]
    return sentence_list


def remove_i():
    """ This function returns a list of subtitles (each item is a subtitle) with 'i'
        removed on the first and last place """
    subtitles_list_without_i = []
    for i in tokenize():
        if i[0] != 'i' and i[-1] != 'i':
            subtitles_list_without_i += [i]
        else:
            subtitles_list_without_i += [i[2:-2]]
    return subtitles_list_without_i


def time():
    subtitle_token = subtitles_open()
    time_list = []
    for subtitle in subtitle_token:
        # time_list += [[i.start, i.end]]
        # print(subtitle.start, '>', subtitle.end)
        time_list += [' '.join([str(subtitle.start), '>', str(subtitle.end)])]
    return time_list


# def get_time():
#     subtitle_token = subtitles_open()
#     time_list = []
#     for i in subtitle_token:


# def compare():
#     dialogues = count_whitespace1()
#     subtitles = remove_i()
#     count = 0
#     for i in subtitles:
#         if i in dialogues:
#             print(i)
#             count += 1
#     print(count)


def compare():
    dialogues = dialogue()
    subtitles = remove_i()
    count = 0
    count_unmatch = 0
    i_count = 0
    match_index = {}
    for i in subtitles:
        i_count += 1
        if i in dialogues:
            # print(i, subtitles.index(i))
            # match_index[i] = subtitles.index(i)
            match_index.setdefault(i, []).append(subtitles.index(i))
            match_index.setdefault(i, []).append(dialogues.index(i))
            count += 1
        else:
            count_unmatch += 1
    return match_index
    # print(i_count)
    # print(count)
    # print(count_unmatch)


def script_time():
    values = compare().values()
    index_list = list(values)
    correct_time_subtitles = []
    script = []
    for i in index_list:
        correct_time_subtitles += [time()[i[0]]]
        script += [dialogue()[i[1]]]
        # print(time()[i], i)
    # print(index_list)
    # print(correct_time_subtitles)
    return index_list


def insert_time_in_script():
    script = count_whitespace1()
    values = compare().values()
    index_list = list(values)
    for i in index_list:
        script.insert(count_whitespace1()[i[1]], time()[i[0]])
    return script


def main():
    print(script_time())


if __name__ == '__main__':
    main()
