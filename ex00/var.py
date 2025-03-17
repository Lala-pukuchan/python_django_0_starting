def my_type(var):
    print(f"{var} has a type {type(var)}")


def my_var():
    my_type(42)
    my_type("42")
    my_type("quarante-deux")
    my_type(42.0)
    my_type(True)
    my_type([42])
    my_type({42: 42})
    my_type((42,))
    my_type(set())


if __name__ == "__main__":
    my_var()
