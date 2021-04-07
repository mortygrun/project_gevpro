#!/bin/python3
# Program: strip_tokenize.py
# Author: Tian Niezing
# Date: 07-04-2021
#

# To use the nltk module, install it by using the following commands in the Linux terminal:
# pip install --user -U nltk
# import nltk
# nltk.download('punkt')


from nltk.tokenize import sent_tokenize


def remove_start_space(file):
    """"This function takes a text file as input and returns the same file without
        title description and without the first 5 white spaces of each line"""
    with open(file) as f:
        content = f.readlines()
    text = []
    for line in content[10:]:
        text.append(line[5:])
    return ''.join(text)


def sentence_tokenize():
    """This function takes the text string from 'remove_start_space' as input and
        prints each sentence separated as elements in a list"""
    # with open(file) as f:
    #     content = f.readlines()
    # text = ''.join(content)
    print(sent_tokenize(remove_start_space('mi.txt')))
    # print(text)


sentence_tokenize()

