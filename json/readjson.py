import json

filename = 'num.json'
with open(filename) as f:
    num = json.load(f)

print(num)
