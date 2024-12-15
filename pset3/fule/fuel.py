while True:
    try:
        x,y = map(int,input("Fraction: ").strip().split("/"))
        # Check if Y is zero
        if y == 0:
            raise ZeroDivisionError

        # Check if X is greater than Y
        if x > y:
            raise ValueError

        # Calculate percentage
        percentage = (x / y) * 100

        # Handle edge cases for empty or full tanks
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")
        break  # Exit loop once valid input is provided

    except (ValueError, ZeroDivisionError):

        x,y = map(int,input("Fraction: ").strip().split("/"))
