#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    set_sum = 0
    for x in my_set:
        set_sum += x
    return set_sum
