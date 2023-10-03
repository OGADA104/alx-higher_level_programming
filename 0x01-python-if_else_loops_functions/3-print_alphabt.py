#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) != 'q' and chr(char_code) != 'e':
        print("{:c}".format(char_code), end='')
