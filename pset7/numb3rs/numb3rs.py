import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to match an IPv4 address
    # Ensure there are 4 sets of 1-3 digits separated by dots
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"

    # Check if the format matches
    if re.match(pattern, ip):
        # Split the IP into its 4 parts (octets)
        parts = ip.split(".")

        # Ensure each part is a valid number between 0 and 255
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
