import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check if exactly one command-line argument is given
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")

    # Get the filename from the command-line argument
    filename = sys.argv[1]

    # Check if the file has a .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Check if the file exists
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    # Read the CSV file and prepare the data for tabulate
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Get the header row
        table = [header]  # Initialize the table with the header

        for row in reader:
            table.append(row)  # Add each subsequent row to the table

    # Print the table formatted as ASCII art
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
