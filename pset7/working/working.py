import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the time format
    pattern = r"(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)"

    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    # Extracting times
    start_time, _, start_period, end_time, _, end_period = match.groups()

    # Convert the times
    start_24 = convert_to_24_hour(start_time, start_period)
    end_24 = convert_to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    # Split time into hours and minutes
    if ":" in time:
        hours, minutes = map(int, time.split(":"))
    else:
        hours = int(time)
        minutes = 0

    # Validate time
    if hours > 12 or minutes >= 60:
        raise ValueError("Invalid time")

    # Convert hours based on AM/PM
    if period == "AM" and hours == 12:
        hours = 0
    elif period == "PM" and hours != 12:
        hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
