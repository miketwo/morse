# -*- coding: utf-8 -*-

# Morse Code Translation Project
# For any alpha numeric input translate the input into morse code
# using the following guidelines:

# 1. Use the table at the following web address as a guide:
# https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg

# 2. Ignore case
# 3. Put spaces ' ' between individual letters and pipes '|' between words
# 4. So the fragments "abc 123" would translate to .- -... -.-.|.---- ..--- ...--

# omit punctuation

# Nice to have
#          1. Translating from morse code to text
#          2. Integrating with an api
#          3. Test Driven

import string

GLOBAL_TRANSLATION_DICT = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '|',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        }


# Create the reverse so we can also go from morse to text
GLOBAL_REVERSE_TRANSLATION = dict((v, k) for (k, v) in GLOBAL_TRANSLATION_DICT.items())
GLOBAL_REVERSE_TRANSLATION[' '] = ''


def clean_up_string(aString):
    tmp = aString.upper()
    tmp = tmp.translate(None, string.punctuation)
    tmp = tmp.strip()
    return tmp


def encode(aString):
    tmp = clean_up_string(aString)
    # This next line converts each character in the string by using the
    # translation hash, joining them all with spaces.
    tmp = " ".join(map(lambda x: GLOBAL_TRANSLATION_DICT[x], tmp))
    tmp = tmp.replace(" | ", "|")
    return tmp


def decode(morse):
    morse = morse.replace("|", " | ")
    # we split into words in order to covert by groups instead of character-by-
    # character
    morse = morse.split()
    tmp = "".join(map(lambda x: GLOBAL_REVERSE_TRANSLATION[x], morse))
    return tmp
