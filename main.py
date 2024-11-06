#!/usr/bin/env python3 

def word_counter(text: str) -> int:
    return(len(text.split()))

def char_counter(text: str) -> dict:
    cc_dict = {}
    for cc in text.lower():
        if cc.isalpha():
            cc_dict[cc] = cc_dict.get(cc,0) + 1
    return cc_dict

def get_book_text(text):
    with open(text) as fh:
        return fh.read()


def main():
    cc_dict = {}
    book_path = './books/frankenstein.txt'
    word_count = 0

    text = get_book_text(book_path)
    word_count = word_counter(text)
    cc_dict = char_counter(text)
    cc_dict_sorted = sorted(cc_dict.items(),reverse=True, key=lambda item: item[1])

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for k, v in cc_dict_sorted:
        print(f"The {k} character was found {v} times")

if __name__ == '__main__':
    main()
