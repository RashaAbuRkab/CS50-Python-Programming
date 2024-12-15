import random

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:  # Level must be a positive integer
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_guess():
    while True:
        try:
            r = int(input("Guess: "))
            if r > 0:  # Guess must be a positive integer
                return r
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    n = get_level()  # Get a valid level
    g = random.randint(1, n)  # Generate a random number between 1 and n

    while True:
        r = get_guess()  # Get a valid guess
        if r < g:
            print("Too small!")
        elif r > g:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop if the guess is correct

if __name__ == "__main__":
    main()
