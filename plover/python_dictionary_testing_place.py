"""
Purpose: Basic python dictionary testing ground
Required Plover Plugins:
    - plover-python-dictionary (https://pypi.org/project/plover-python-dictionary/)

Requires installing pyperclip using plover_console program
example running on windows:
& "C:\Program Files\Open Steno Project\Plover 4.0.0\plover_console.exe"  -s plover_plugins install pyperclip
Which is pretty much just like running pip install ....
"""

import re
import pyperclip

LONGEST_KEY = 1


def lookup(key):
    assert len(key) <= LONGEST_KEY

    """
    Command to take the system clipboard text and wrap it for a sql
    query. For example copying the following lines
    123
    567
    789

    And triggering this command will result in:
    '123','567','789'
    """
    if key[0] == 'PA*EFT':
        return ','.join(map(lambda line: f"'{line.strip()}'", pyperclip.paste().splitlines()))

    raise KeyError
