def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    output = ""
    for i in word:
        # Check if the character is a vowel (both uppercase and lowercase)
        if i.lower() not in "aeiou":
            output += i
    return output


if __name__ == "__main__":
    main()
