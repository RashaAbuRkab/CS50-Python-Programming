def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check if the first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    has_number = False

    for i in range(len(s)):
        # If the character is a digit
        if s[i].isdigit():
            if not has_number:
                # First digit cannot be a 0
                if s[i] == '0':
                    return False
            has_number = True
        # Once we encounter a number, no letters should follow
        elif has_number:
            return False
        # Disallow non-alphanumeric characters
        if not s[i].isalnum():
            return False

    return True



main()
