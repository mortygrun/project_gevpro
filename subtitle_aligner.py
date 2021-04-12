import nltk
import re
import pysrt
from nltk.tokenize import RegexpTokenizer


def text_open():
    with open('mi.txt') as f:
        return f.readlines()


def subtitles_open():
    subs = pysrt.open('mi_opy.srt')
    return subs


def tokenize():
    tokenizer = RegexpTokenizer(r'\w+')
    text_token = text_open()
    subtitle_token = subtitles_open()
    sentence_list = []
    time_list = []
    for i in subtitle_token:
        sentence_list += [tokenizer.tokenize(i.text)]
    # for i in subtitle_token:
        # time_list += [[i.start, i.end]]
    # print(time_list)


def tokenize_text():
    pass


if __name__ == '__main__':
    tokenize()
