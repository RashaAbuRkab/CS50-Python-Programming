def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length of the plate
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Check if it contains only alphanumeric characters
    if not s.isalnum():
        return False

    # Initialize a flag to determine if a number has been encountered
    number_found = False

    for i in range(len(s)):
        if s[i].isdigit():
            # If the number starts with a '0', it's invalid
            if s[i] == '0' and not number_found:
                return False
            # If a number is encountered, set the flag
            number_found = True
        elif number_found and s[i].isalpha():
            # If a number was already found and now a letter is found, it's invalid
            return False

    return True


if __name__ == "__main__":
    main()
