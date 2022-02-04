#!/usr/bin/python
"""Write raw steno stroke on next stroke
Adapted from: https://pypi.org/project/plover-python-dictionary/
Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
"""

LONGEST_KEY = 2

command = "TPHR*EU"


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if command != key[0]:
        raise KeyError
    if len(key) == 1:
        return "{#}"

    return "dog dog dog " + key[1]
