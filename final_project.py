import re
from nltk.tokenize import RegexpTokenizer
import pysrt

def file_opener():
    with open('mi.txt') as f:
        return f.readlines()

def script_editor():
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
        elif count_indent >= 26:
            all_text_list += ['C|', i]
        elif 16 <= count_indent < 26 and not i.strip().startswith('(') and not i.isupper():
            dialogue_list += [' '.join(tokenizer.tokenize(i.strip()))]
            all_text_list += ['D|', i]
        elif 3 < count_indent < 16 and bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
            all_text_list += ['S|', i]
        elif 3 < count_indent < 16 and not bool(re.match(r'[A-Z]+$', ''.join(tokenizer.tokenize(i)))):
            all_text_list += ['N|', i]
        elif i.strip().startswith('(') and i.strip().endswith(')'):
            all_text_list += ['M|', i]
        else:
            all_text_list += [' |', i]

    return ''.join(all_text_list)

def dialogue_stripper():
    """Returns list with only dialogue"""
    string = file_opener()
    tokenizer = RegexpTokenizer(r'\w+')

    dialogue_list = []

    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if 16 <= count_indent < 26 and not i.strip().startswith('(') and not i.isupper():
            dialogue_list += [' '.join(tokenizer.tokenize(i.strip()))]

    return dialogue_list


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
        time_list += [' '.join([str(subtitle.start), '>', str(subtitle.end)])]
    return time_list

def dialogue():
    string = file_opener()
    tokenizer = RegexpTokenizer(r'\w+')

    dialogue_list = []

    for i in string:
        count_indent = len(i) - len(i.lstrip())
        if 16 <= count_indent < 26 and not i.strip().startswith('(') and not i.isupper():
            dialogue_list += [' '.join(tokenizer.tokenize(i.strip()))]
            print(' '.join(tokenizer.tokenize(i.strip())))
    # return dialogue_list

def compare():
    dialogues = dialogue_stripper()
    subtitles = remove_i()
    count_total = 0
    count_match = 0
    count_unmatch = 0
    for i in subtitles:
        count_total += 1
        if i in dialogues:
            count_match += 1
        else:
            count_unmatch +=1
    print('Total amount of lines of dialogue:',count_total)
    print('Total amount of lines of dialogue that match with subtitles:', count_match)
    print('Total amount of lines of dialogue that do not match with subtitles:', count_unmatch)
    print('Percentage matched:', round(count_match/count_total*100),'%')
    print('Percentage unmatched:', round(count_unmatch/count_total*100),'%')

def main():
    f = open("newscript.txt","w")
    f.write(script_editor())
    f.close()
    print(compare())


if __name__ == '__main__':
    main()
