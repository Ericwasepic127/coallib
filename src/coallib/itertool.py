#!/usr/bin/env python3
# Made by @Ericwasepic127

"""
Iterable things helper
"""

def get_last_index(iterable) -> int:
    """Returns last index of iterable"""
    assert iterable, "Iterable is empty!"
    assert hasattr(iterable, "__iter__"), "Gave non-iterable object!"
    return len(iterable) - 1

def get_fixed_string(string: str, remove: str=" ") -> str:
    """Deletes trailing spaces or from remove argument"""
    from .iftool import raise_type
    raise_type(string, str)
    raise_type(remove, str)
    return string.strip().rstrip()

def full_fix_str(string: str) -> str:
    """Removes any trailing space and newlines"""
    return get_fixed_string(get_fixed_string(string), "\n")

