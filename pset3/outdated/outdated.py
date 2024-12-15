# Dictionary to map month names to their corresponding numbers
months = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

while True:
    # Prompt the user for input
    date_input = input("Date: ").strip()

    try:
        # Check if the input is in MM/DD/YYYY format
        if "/" in date_input:
            month, day, year = date_input.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            # Validate that the month is between 1 and 12 and the day is between 1 and 31
            if 1 <= month <= 12 and 1 <= day <= 31:
                # Format and print the date in YYYY-MM-DD format
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

        # Check if the input is in "Month day, year" format
        else:
            month_name, day_year = date_input.split(" ", 1)
            day, year = day_year.split(", ")
            day = int(day)
            year = int(year)

            # Validate that the month name is valid and the day is between 1 and 31
            if month_name in months and 1 <= day <= 31:
                # Convert the month name to its corresponding number and print the date
                month = months[month_name]
                print(f"{year:04d}-{month}-{day:02d}")
                break

    except (ValueError, IndexError):
        # If there's any error, prompt the user again
        pass
