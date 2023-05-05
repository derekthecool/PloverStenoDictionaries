"""
Purpose: Pull file from local file system
(staying inside this repo for better portability)
"""

import os.path
import pathlib
import sys

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 2

platform = sys.platform
if platform == "win32":
    BASE_PATH = os.path.join(os.getenv("LOCALAPPDATA"), "plover", "plover")
elif platform == "linux":
    BASE_PATH = os.path.join(os.getenv("HOME"), ".config", "plover", "plover")

online_snippet_dictionary = {
    # lua
    "HRAOU": "clash-of-code.lua",

    # C#
    "SHA*RP": "clash-of-code.cs",

    # C++
    "KPR-P": "clash-of-code.cpp",

    # F#
    "TPA*RP": "clash-of-code.fs",

    # bash
    "PWARB": "clash-of-code.sh",

    # bash
    "KR*": "clash-of-code.c",
}


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] == "TP*ET" and len(key) > 1:
        filename = os.path.join(
            BASE_PATH, "local_snippets", online_snippet_dictionary.get(key[1])
        )
        exists = os.path.isfile(filename)
        # return str(exists)
        if exists:
            f = open(filename, "r")
            return f.read()
        else:
            raise KeyError
    else:
        raise KeyError
