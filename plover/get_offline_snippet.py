"""
Purpose: Pull file from local file system
(staying inside this repo for better portability)
"""

import os.path
import pathlib
import sys
import subprocess

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 2

platform = sys.platform
if platform == "win32":
    plover_base_path = os.path.join(os.getenv("LOCALAPPDATA"), "plover", "plover")
    clipboard_command = 'clip'
elif platform == "linux":
    plover_base_path = os.path.join(os.getenv("HOME"), ".config", "plover", "plover")
    clipboard_command = 'pbcopy'
elif platform == "darwin":
    # Never tested
    plover_base_path = os.path.join(os.getenv("HOME"), "Library", "Application Support", "plover")
    clipboard_command = 'pbcopy'


online_snippet_dictionary = {
    # lua
    "HRAOU": "clash-of-code.lua",
    "TPUPB": "lua-fun-minified.lua",

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
            plover_base_path, "local_snippets", online_snippet_dictionary.get(key[1])
        )
        exists = os.path.isfile(filename)
        # return str(exists)
        if exists:
            f = open(filename, "r")

            # Setting the clipboard is faster than Plover "typing" out the text
            # Longer texts get mangled when printed by Plover
            # Make sure to set shell=True or it'll open a terminal window briefly
            subprocess.run(clipboard_command, text=True, input=f.read(), shell=True)
            return '{#Control_L(v)}'
        else:
            raise KeyError
    else:
        raise KeyError
