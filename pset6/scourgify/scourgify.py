import csv
import sys
import os

def main():
    # Check if exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists and can be opened
    if not os.path.isfile(input_file):
        sys.exit(f"Could not read {input_file}")

    # Process the input CSV file and write to the output CSV file
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)

        # Write the header for the output file
        writer.writerow(["first", "last", "house"])

        for row in reader:
            # Split the name into first and last
            full_name = row['name'].split(", ")
            last_name = full_name[0]
            first_name = full_name[1]
            house = row['house']

            # Write the split names and house to the new CSV
            writer.writerow([first_name, last_name, house])

if __name__ == "__main__":
    main()
