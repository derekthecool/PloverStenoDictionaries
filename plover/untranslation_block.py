import re
"""
This dictionary blocks untanslated items.
However, there is an exception to help Plover folding items to make it through.
If a chord ends in LGTSDZ then I'll let it through.

This seems to be the best solution for now (now being 2022-11-08)
"""

LONGEST_KEY = 1
def lookup(chord):
    if not re.match(r'.*[LGTSDZ]+$', chord[0]):
        return '{null}'
