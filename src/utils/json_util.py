"""
json ultilities
"""
import json


def is_json(myjson: str):
    """check if input string is valid json format or not

    Args:
        myjson (string): json string

    Returns:
        bool: True if `myjson` is valid json format otherwise return False
    """
    try:
        json.loads(myjson)
    except ValueError as _:
        return False
    return True
