def main():
    amount_due = 50  # Total amount due
    amount_inserted = 0  # Track amount inserted by the user

    while amount_inserted < 50:
        # Prompt user to insert a coin
        insert = int(input("Insert Coin: "))

        # Check if the coin is valid
        if insert in [25, 10, 5]:
            amount_inserted += insert
            # Calculate remaining amount due
            amount_due = 50 - amount_inserted

            # Inform user of the amount due (if any)
            if amount_due > 0:
                print(f'Amount Due: {amount_due}')
        else:
            print(f'Amount Due: {amount_due}')  # Invalid coin input; show amount due

    # Calculate change owed
    change_owed = amount_inserted - 50
    print(f'Change Owed: {change_owed}')

if __name__ == "__main__":
    main()
