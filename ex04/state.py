import sys


def state_search():
    if len(sys.argv) != 2:
        return

    capital = sys.argv[1]
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    for state_name, abbr in states.items():
        if capital_cities.get(abbr) == capital:
            print(state_name)
            return

    print("Unknown capital city")


if __name__ == '__main__':
    state_search()
