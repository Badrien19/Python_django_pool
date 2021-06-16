# -*- coding: utf-8 -*-
import sys


def find_by_key(src_dict, niddle):
    if niddle in src_dict.keys():
        return ((niddle, src_dict[niddle]))
    return(None)

def find_by_value(src_dict, niddle):
    if niddle in src_dict.values():
        for key, value in src_dict.items():
            if value == niddle:
                return ((key, value))
    return(None)

def find_match(cible):
    states = {
        "Oregon"    : "OR",
        "Alabama"   : "AL",
        "New Jersey": "NJ",
        "Colorado"  : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    search = find_by_key(states, cible)
    if search:
        return ({'capital': capital_cities[search[1]], 'state': search[0]})
    else:
        capital_search = find_by_value(capital_cities, cible)
        if capital_search:
            return ({'capital': capital_search[1], 'state': find_by_value(states, capital_search[0])[0]})
    return (None)


def run(cible):
    liste = cible.split(',')
    for i in liste:
        i = i.rstrip().lstrip().title()
        if i:
            result = find_match(i)
            if result:
                print("%s is the capital of %s" % (result['capital'], result['state']))
            else:
                print("%s is neither a capital city nor a state" % i)


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        run(sys.argv[1])