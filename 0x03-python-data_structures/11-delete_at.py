#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    if 0 < idx > len(my_list) - 1:
        return my_list
    if idx > 0:
        del my_list[idx]
    return my_list
