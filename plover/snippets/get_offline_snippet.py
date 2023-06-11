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
    plover_base_path = os.path.join(
        os.getenv("LOCALAPPDATA"), "plover", "plover", "snippets", "snippets"
    )
    clipboard_command = "clip"
elif platform == "linux":
    plover_base_path = os.path.join(
        os.getenv("HOME"), ".config", "plover", "plover", "snippets", "snippets"
    )
    clipboard_command = "pbcopy"
elif platform == "darwin":
    # Never tested
    plover_base_path = os.path.join(
        os.getenv("HOME"),
        "Library",
        "Application Support",
        "plover",
        "snippets",
        "snippets",
    )
    clipboard_command = "pbcopy"


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] == "TP*ET" and len(key) > 1:
        # Recurse file system: https://stackoverflow.com/a/3207973/9842112
        files = []
        for base, _, file_list in os.walk(plover_base_path):
            for current_file in file_list:
                files.append(os.path.join(base, current_file))

        steno_key = key[1]

        # Replace * in the raw steno with lowercase s. This is just my first
        # shot at supporting the * key, as this is not allowed in a file path
        steno_key.replace("*", "s")

        # Special case to list out all snippet dictionary files
        list_snippets_steno_keyword = "STPHEUPT"
        if steno_key == list_snippets_steno_keyword:
            return str(files)

        # Normal use case to to check for file with matching key as start of
        # file path
        filename = ''
        for file in files:
            if steno_key in file:
                filename = file

        if os.path.isfile(filename):
            f = open(filename, "r")

            # Setting the clipboard is faster than Plover "typing" out the text
            # Longer texts get mangled when printed by Plover
            # Make sure to set shell=True or it'll open a terminal window briefly
            subprocess.run(clipboard_command, text=True,
                           input=f.read(), shell=True)

            # Paste output with control + v
            return "{#Control_L(v)}"
        else:
            raise KeyError
    else:
        raise KeyError
