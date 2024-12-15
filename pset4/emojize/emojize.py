import emoji

# Get input from the user (no prompt text)
text = input().strip()  # Read input without any prompt

# Convert the emoji codes in the input to emojis
output = emoji.emojize(text,language='alias')

# Print the output
print(output)
