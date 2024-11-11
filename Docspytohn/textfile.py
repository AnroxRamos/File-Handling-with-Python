# Reading a text file
with open('file.txt', 'r') as file:
    content = file.read()

# Writing to a text file
with open('file.txt', 'w') as file:
    file.write("This is a new line of text.")

# Appending to a text file
with open('file.txt', 'a') as file:
    file.write("\nAdditional line of text.")
