#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        print("{}".format(chr(char_code)), end='')
    print("")
