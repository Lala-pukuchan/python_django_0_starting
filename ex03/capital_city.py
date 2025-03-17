import sys


def capital_city():
    if len(sys.argv) != 2:
        return

    state = sys.argv[1]
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

    if state in states:
        abbr = states[state]
        print(capital_cities.get(abbr, "Unknown state"))
    else:
        print("Unknown state")


if __name__ == "__main__":
    capital_city()
