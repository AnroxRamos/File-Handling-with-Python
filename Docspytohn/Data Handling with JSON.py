import json

# Writing to a JSON file
data = {"ID": 1, "Name": "Anna"}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# Reading a JSON file
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)
