#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    add = calc.add(a, b)
    print("{} + {} = {}".format(a, b, add))
    sub = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, sub))
    mul = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, mul))
    div = calc.div(a, b)
    print("{} / {} = {}".format(a, b, div))
