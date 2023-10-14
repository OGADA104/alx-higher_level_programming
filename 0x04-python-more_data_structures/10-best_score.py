#!/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    score = float('-inf')
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            best = key
    return best