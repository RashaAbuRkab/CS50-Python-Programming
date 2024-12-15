def main():
    camel_case = input("Enter a variable name in camel case: ")
    snake_case = convert(camel_case)
    print(snake_case)

def convert(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            # Add an underscore before the uppercase character, and convert it to lowercase
            snake_case += "_" + char.lower()
        else:
            # Add the lowercase character directly
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()
