# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
    

# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# # print(f'{pi_string[:92]}...')
# # print(len(pi_string))
# birtday = input('You:r birtday: ')
# if birtday in pi_string:
#     print('Yes')
# else:
#     print("No")


# with open('learning_python.txt') as object:
#     obj = object.read()
    
# print(obj)
nnn = []
with open('learning_python.txt') as object:
    obj = object.readlines()
for i in obj:
    nnn.append(i.replace('Python','C'))
for i in nnn:
    print(i.rstrip())
    



