#!/usr/bin/python3
"""load , add and save json data"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

try:
    data = load_from_json_file(file_name)
except FileNotFoundError:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(file_name, data)
