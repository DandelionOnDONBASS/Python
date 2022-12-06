import json


def fav_num():
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            favor_number = json.load(f)
    except FileNotFoundError:
        with open(filename,'w')as f:
            favor_number = input('Enter you number: ')
            json.dump(favor_number,f)
            print(f'You favorite number is {favor_number}')
    except json.decoder.JSONDecodeError:
        with open(filename,'w')as f:
            favor_number = input('Enter you name: ')
            json.dump(favor_number,f)
            print(f'You favorite number is {favor_number}')
    else:
        print(f'your favorite number is,{favor_number}')

fav_num()


