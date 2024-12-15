import validators

def main():
    # Prompt user for an email address
    email = input("Please enter your email address: ")

    # Validate the email address
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
