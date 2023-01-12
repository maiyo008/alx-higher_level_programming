#!/usr/bin/python3
# 3-to_json_string.py

import json
"""Defines a file-writing function."""

def to_json_string(my_obj):
    """Return JSON representation of an object(string)

    Args:
        my_obj (str): The string to be converted to JSON

    Returns:
         JSON representation of my_obj
    """
    return json.dumps(my_obj)
