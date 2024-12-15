def main():
    time = input("What time is it? ").strip()
    hours = convert(time)

    # Check if the time falls within breakfast, lunch, or dinner time
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    # Convert the time into hours as a float (e.g., 7:30 becomes 7.5)
    return float(hour) + float(minute) / 60

if __name__ == "__main__":
    main()
