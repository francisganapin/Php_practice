import json

# Open the JSON file and load the data
with open('data/users.json') as f:
    data = json.load(f)

# Iterate over each user to extract and print their names as lists of characters
for user in data:
    print((user['name']))