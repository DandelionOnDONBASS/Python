"""Создание гостевой книги с приветствием"""
# # enter_name = input("Hello our new client, what is your name?")
# filename = ('guest_book.txt')
# k = 0
# users = []
# while k!= 5:
#     with open(filename,'a') as file_name:
#         enter_name = input("Hello our new client, what is your name? \nEnter your name: ")
#         file_name.write('Hello our client ')
#         file_name.write(f'{enter_name.title()}')
#         file_name.write(f', Welcome to oure restaurant!!!\n')
#         users.append(enter_name)
#         k+=1
# """выводит какие клиенты были добавлены в список"""
# k=1
# print('\nIts our new clients:')
# for i in users:
#     print(f'{k}\t{i.title()}')
#     k+=1



filename = ('guest_book.txt')
k = 0
users = []
while k!= 5:
    with open(filename,'a') as file_name:     
        enter_name = input("Hello our new client, what is your name? \nEnter your name: ")
        file_name.write('Hello our client ')
        file_name.write(f'{enter_name.title()}')
        file_name.write(f', Welcome to oure restaurant!!!\n')
        file_name.write(f'\t{enter_name.title()} like programing because:')
        quation = input('Why do you like programming?\n Please enter where: \n')
        file_name.write(f'{quation}\n')
        users.append(enter_name)
        k+=1
        # while enter_name != '':
        #     with open(filename,'a')as file_name:
        #         quation = input('Why do you like programming?\n Please enter where: \n')
        #         file_name.write(quation)
        #         break
"""выводит какие клиенты были добавлены в список"""
k=1
print('\nIts our new clients:')
for i in users:
    print(f'{k}\t{i.title()}')
    k+=1
    tr