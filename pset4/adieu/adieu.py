import inflect

# Create an inflect engine instance
p = inflect.engine()

# List to store the names
names = []

# Continuously prompt the user for names
print("Enter names (Ctrl-D to finish):")
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break

# Join the names with proper grammar using inflect
farewell = "Adieu, adieu, to " + p.join(names)

# Print the formatted farewell
print(farewell)
