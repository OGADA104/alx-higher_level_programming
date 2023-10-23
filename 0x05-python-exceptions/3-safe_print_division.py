#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            result = a / b
        else:
            results = None
    except:
        result = None
    finally:
        print("Inside result:{}".format(result))
    return result
