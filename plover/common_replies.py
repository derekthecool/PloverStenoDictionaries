import random

"""
Cool web apis to possibly integrate:
    - https://dictionaryapi.dev/ which requires no api key and returns definitions and more

Cool GitHub projects that might be super useful for creating phrases
    - https://github.com/dariusk/corpora - contains lots and lots of json lists
"""

LONGEST_KEY = 2

STARTER = "KPHOPB"

LOOKUP = {
    # yes phrases
    'KWRE': [
        "that is great",
        "I like that idea",
        "good plan, that will work",
    ],

    # no phrases
    'TPHO': ["no", "no, that won't work", "that doesn't sound right"],
}


def lookup(key):
    assert len(key) <= LONGEST_KEY
    phrase_list = LOOKUP[key[len(key) - 1]]
    if len(key) == 2 and key[0] == STARTER and phrase_list:
        return random.choice(phrase_list)
    raise KeyError
