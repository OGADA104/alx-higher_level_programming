#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r_list = my_list.copy()
    for x in r_list:
        if r_list[x] == search:
            r_list[x] = replace
        return r_list
