#!/usr/bin/python3
for i in range( 0, 100, 1):
    print("{0}".format(i), end= '')
    if i < 99:
        print(", ", end= '')
    else:
        print("")
