print('Give me two numbers, and I"ll divide them.')
while True:
    try:
        first_number = int(input('\nFirst number: '))
        second_number = int(input('Second Number: '))
        ent = input('Введите действие *,/,-,+')
        if ent =="-":
            a = first_number - second_number
        elif ent == "*":
            a =first_number * second_number
        elif ent == "/":
            a  = first_number / second_number
        elif ent == "+":
            a = first_number + second_number
    except ValueError:
        print('Вводить цифры!')
    except ZeroDivisionError:
        print('НА ноль делить нельзя!')
    else:
        print(f'{first_number} {ent} {second_number} = {a}')