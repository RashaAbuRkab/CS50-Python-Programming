import random

def main():
    level = get_level()  # Get the level from the user
    score = 0  # Initialize the score

    # Loop through 10 problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        # Allow up to 3 attempts per problem
        while attempts < 3:
            try:
                # Prompt the user for an answer
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1  # Increment score if the answer is correct
                    break  # Move on to the next problem
                else:
                    print("EEE")  # Display error for incorrect answer
                    attempts += 1
            except ValueError:
                print("EEE")  # Handle non-numeric input
                attempts += 1

        # After 3 incorrect attempts, show the correct answer
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # At the end, display the final score
    print(f"Score: {score}/10")


def get_level():
    """Prompt the user for a level (1, 2, or 3)"""
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:  # Ensure the input is 1, 2, or 3
                return level
        except ValueError:
            pass  # Ignore invalid inputs and reprompt


def generate_integer(level):
    """Generate a random integer based on the level"""
    if level == 1:
        return random.randint(0, 9)  # Single-digit integers for level 1
    elif level == 2:
        return random.randint(10, 99)  # Two-digit integers for level 2
    elif level == 3:
        return random.randint(100, 999)  # Three-digit integers for level 3
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
