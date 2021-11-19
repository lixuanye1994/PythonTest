import json

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filename = 'num.json'
with open(filename, 'w') as f:
    json.dump(num, f)