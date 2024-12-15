def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


def convert(fraction):
    # Split the input string into x and y
    try:
        x, y = fraction.split('/')
        x = int(x)  # Convert x to integer
        y = int(y)  # Convert y to integer
    except ValueError:
        raise ValueError("X and Y must be integers.")

    if y == 0:
        raise ZeroDivisionError("Y cannot be zero.")
    if x > y:
        raise ValueError("X cannot be greater than Y.")


    # Calculate percentage and round to the nearest integer
    percentage = round((x / y) * 100)
    # Ensure the percentage is between 0 and 100
    return max(0, min(percentage, 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"  # Label for empty
    elif percentage >= 99:
        return "F"  # Label for full
    else:
        return f"{percentage}%"  # Return the percentage with a percent sign


if __name__ == "__main__":
    main()
