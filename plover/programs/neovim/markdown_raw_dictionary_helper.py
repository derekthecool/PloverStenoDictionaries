#!/usr/bin/python
"""Write raw steno stroke on next stroke
Adapted from: https://pypi.org/project/plover-python-dictionary/
Requirements:
    - python dictionary plugin (https://pypi.org/project/plover-python-dictionary/)
"""

LONGEST_KEY = 10
START_SEQUENCE = "RAUS"
# My Emilys symbols mapping for a colon with spaces on both sides ' : '
STOP_SEQUENCE = "SKWHAOLG"


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] != START_SEQUENCE:
        raise KeyError

    # Print a help prompt when entering this mode
    # After sending any other keys the prompt deletes
    if key[0] == START_SEQUENCE and len(key) == 1:
        return "Enter raw steno string and have it joined with '/' STOP=stop"

    if STOP_SEQUENCE in str(key[1:]):
        raise KeyError

    return "/".join(key[1:])
