"""
Purpose: Pull file from the web and insert as text

2023-05-03: works but takes a several minutes and the contents start messing up
after a while. Should work for content that is maybe 100 lines
"""

import urllib.request

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 2

online_snippet_dictionary = {
    # lua
    "HRAOU": "https://raw.githubusercontent.com/luafun/luafun/master/fun.lua",

    # test
    "TEFT": "https://raw.githubusercontent.com/protobuf-c/protobuf-c/master/LICENSE",
}


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] == "TKPW*ET" and len(key) > 1:
        url = ""
        url = online_snippet_dictionary.get(key[1])
        if url:
            return urllib.request.urlopen(url).read().decode("utf-8")

    else:
        raise KeyError


def reverse_lookup(text):
    return []
