#!/usr/bin/python3
import sys
argv = sys.argv
argc = len(argv)
sum1 = 0
if __name__ == "__main__":
    for x in range(1, argc):
        h = argv[x]
        sum1 += int(h)
    print("{}".format(sum1))
