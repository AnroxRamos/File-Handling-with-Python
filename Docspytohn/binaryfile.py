# Reading a binary file
with open('image.bin', 'rb') as file:
    data = file.read()

# Writing to a binary file
with open('image.bin', 'wb') as file:
    file.write(data)
