#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    at_index = my_list[idx]
    return at_index
