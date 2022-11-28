import json

# Opening JSON file
f = open('jsonTreeDict.json')

# returns JSON object as 
# a dictionary
data = json.load(f)
print(len(data[0]))

# Iterating through the json
# list
for i in range(len(data[0])):
    print(data[0][i])
    print("")