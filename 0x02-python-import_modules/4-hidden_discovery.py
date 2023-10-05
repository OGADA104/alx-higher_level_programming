#!/usr/bin/python3
import dis
if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        bytecode = file.read()
    dis.dis(bytecode)
