import sys


def all_in():
    if len(sys.argv) != 2:
        return

    arg = sys.argv[1]
    tokens = arg.split(",")

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

    capital_to_states = {
        capital_cities[abbr].lower(): state for state, abbr in states.items()
    }
    states_to_capitals = {
        state.lower(): capital_cities[abbr] for state, abbr in states.items()
    }

    for token in tokens:
        if token.strip() == "":
            continue
        normalized = token.strip().lower()
        found = False
        if normalized in capital_to_states:
            state = capital_to_states[normalized]
            cap = states_to_capitals[state.lower()]
            found = True
        elif normalized in states_to_capitals:
            cap = states_to_capitals[normalized]
            state = capital_to_states[cap.lower()]
            found = True
        else:
            found = False

        if found:
            print(f"{cap} is the capital of {state}")
        else:
            original = token.strip()
            print(f"{original} is neither a capital city nor a state")


if __name__ == "__main__":
    all_in()
