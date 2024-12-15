import sys
import os

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check for valid Python file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    n = 0

    # Count lines of code excluding comments and blank lines
    with open(filename) as file:
        for line in file:
            # Strip whitespace from the line
            stripped_line = line.strip()
            # Count lines that are not blank and not comments
            if stripped_line and not stripped_line.startswith("#"):
                n += 1

    print(f"The file contains {n} lines.")

if __name__ == "__main__":
    main()
