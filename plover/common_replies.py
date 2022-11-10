import random

LONGEST_KEY = 2

STARTER = 'KPHOPB'

YES_PHRASES = ['yes', 'yes, that\'ll work', 'perfect', 'sounds good']
NO_PHRASES = ['no', 'no, that won\'t work', 'that doesn\'t sound right']

def lookup(key):
    assert len(key) <= LONGEST_KEY
    if len(key) == 2 and key[0] == STARTER:
        phrase = key[1]
        if phrase == 'KWRE':
            return random.choice(YES_PHRASES)
        if phrase == 'TPHO':
            return random.choice(NO_PHRASES)
    raise KeyError
