dic = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0
while True:
    try:
        # Prompt for item input and format it
        user = input("Item: ").strip().lower()

        # If item is in the menu, add to total
        if user in dic:
            total += dic[user]
            print(f"Total: ${total:.2f}")
        else:
            # Reprompt if the item is not found in the menu
            print("Item not found. Please try again.")

    except EOFError:
        # Exit the loop gracefully on EOF input
        print()
        break
