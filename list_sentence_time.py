from nltk.tokenize import RegexpTokenizer
import pysrt


def text_open():
    with open('mi.txt') as f:
        return f.readlines()


def subtitles_open():
    # You have to save the .srt file with utf-8 first
    subs = pysrt.open('mi_utf8.srt')
    return subs


def tokenize():
    tokenizer = RegexpTokenizer(r'\w+')
    subtitle_token = subtitles_open()
    sentence_list = []
    for i in subtitle_token:
        sentence_list += [tokenizer.tokenize(i.text)]
    return sentence_list


def time():
    subtitle_token = subtitles_open()
    time_list = []
    for i in subtitle_token:
        time_list += [[i.start, i.end]]
    return time_list


def list_of_sentences():
    # print(tokenize())
    print(time())


if __name__ == '__main__':
    list_of_sentences()
