#!/usr/bin/python3
import calculator_1 as calc
if __name__ == "__main__":
    a = 10
    b = 5
    add = calc.add(a, b)
    print(f"{a} + {b} = {add}")
    sub = calc.sub(a, b)
    print(f"{a} - {b} = {sub}")
    mul = calc.mul(a, b)
    print(f"{a} * {b} = {mul}")
    div = calc.div(a, b)
    print(f"{a} / {b} = {div}")
