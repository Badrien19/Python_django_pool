# -*- coding: utf-8 -*-
import sys

def run(cible):
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
    for key, value in capital_cities.items():
        if value == cible:
            for s_key, s_value in states.items():
                if s_value == key:
                    print(s_key)
                    return
    print("Unknown capital city")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        run(sys.argv[1])