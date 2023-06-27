#!/usr/bin/python
"""Write raw steno stroke on next stroke
Adapted from: https://pypi.org/project/plover-python-dictionary/
Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
"""

LONGEST_KEY = 7
START_SEQUENCE = "RAUS"
STOP_SEQUENCE = "STOP"
started = False


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] != START_SEQUENCE:
        raise KeyError
    elif key[0] == START_SEQUENCE and len(key) == 1:
        return "Enter raw steno string and have it joined with '/' STOP=stop"
    else:
        started = True

    if STOP_SEQUENCE in str(key[1:]):
        started = False
        # raise KeyError
        return "/".join(key[1:-1])
        # return ""

    if started:
        return "/".join(key[1:])
    else:
        raise KeyError
