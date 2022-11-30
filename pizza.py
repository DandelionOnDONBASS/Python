def make_pizza(size,*toppings):
    print(f'Making a {size}-inch pizza widt the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')
