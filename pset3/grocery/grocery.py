# Initialize an empty dictionary to store grocery items and their counts
grocery_list = {}

while True:
    try:
        # Prompt for an item and process it (strip leading/trailing spaces, convert to lowercase)
        item = input().strip().lower()

        # Update the count of the item in the dictionary
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        # Break the loop when EOF (Ctrl+D) is encountered
        print()  # Print a newline for formatting
        break

# Output the sorted grocery list
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item.upper()}")
