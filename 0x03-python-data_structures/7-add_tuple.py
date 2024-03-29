#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_add = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_add
    # If either tuple has fewer than 2 elements, pad them with zeros
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0,)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0,)

    # Calculate the sum of corresponding elements based on tuple length
    tuple_add = (tuple_a[0] + tuple_b[0],)
    if len(tuple_a) > 1:
        tuple_add += (tuple_a[1] + tuple_b[1],)
    return tuple_add
