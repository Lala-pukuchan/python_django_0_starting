def print_numbers():
    with open("./numbers.txt", "r") as file:
        content = file.read().strip()

    list = content.split(",")
    for num in list:
        print(num.strip())


if __name__ == "__main__":
    print_numbers()
