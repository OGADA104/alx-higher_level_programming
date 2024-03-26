#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    argc = len(argv)
    if argc < 2:
        print("{} arguments.".format(argc - 1))
    elif 2 <= argc < 3:
        print("{} argument:".format(argc - 1))
        print("{}: {}".format(argc - 1, argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for x in range(1, argc):
            print("{}: {}".format((x), argv[x]))
