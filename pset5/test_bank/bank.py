def main():
    word = input("Greeting: ")
    print(value(word))


def value(greeting):
    if greeting[0:5].lower() == "hello":
        return 0
    elif greeting[0].lower() == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
