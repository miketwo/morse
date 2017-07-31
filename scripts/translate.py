#!/usr/bin/env python
# encoding: utf-8
import argparse
import morse

DESC = '''
DESCRIPTION
translate is a program to translate morse code

USAGE
    # Translate to morse code
    translate.py "text to translate"
    - . -..- -|- ---|- .-. .- -. ... .-.. .- - .

    # Or in reverse
    translate.py -r "- . -..- -|- ---|- .-. .- -. ... .-.. .- - ."
    TEXT TO TRANSLATE

NOTES
    Case is ignored. All text is internally converted to uppercase.
    Punctuation is ignored.
'''


def parse_args():
    parser = argparse.ArgumentParser(
        description=DESC,
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        'text',
        help=("Text or morse code to translate"))

    parser.add_argument(
        '-r', '--reverse', action="store_true",
        help=("Translate morse code back to text"))

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.reverse:
        print morse.translate.decode(args.text)
    else:
        print morse.translate.encode(args.text)


if __name__ == '__main__':
    main()
