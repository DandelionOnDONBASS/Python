import json

numbers = int(input('Enter your favorite number: '))

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)


