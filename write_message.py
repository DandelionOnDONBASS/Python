# # 'w' значит запись, 'а' присоединение, 'r' чтение
# """Добавление имен в текстовый файл и вывод их в терминал"""
# filename = ('guests.txt')
# k = 0
# while k!=5:
#     with open(filename,'a') as file_name:
#         file_name.write('Your name is : ')
#         file_name.write(f'{input("Enter you name: ")}\n')
#         k+=1
# with open(filename) as file_name:
#     user = file_name.readlines()
#     for i in user:
#         print(i.rstrip())
"""Калькулятор с ошибкой"""
# print('Give me two numbers, and I"ll divide them.')
# print('Enter "q" to quit')
# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('Second Number: ')
#     if second_number == 'q':
#         break
#     try:
#         answear = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('You can not divide by 0!')
#     else:
#         print(answear)
"""Файл не найден"""
def count_words(filename):
    try: 
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  #просто пропускаеи ошибку  и программа работает дальше
        #print(f'Sorry, the file {filename} does not exist.')
    else:
        #Посчет приблизительного количества строк в файле
        words = contents.split()
        num_words = len(words)
        #подсчитываем количество символов в filename
        fff=len(filename)
        #отнимаем 4 последних символа в filename
        fff_u_txt= filename[:fff-4]
        #Вывести каждое название книги без расширения
        print(f'The file {fff_u_txt.upper()} has about {num_words} words.')
#Список книг в формате тхт вносим в список
filenames = ['alice.txt','siddharta.txt','moby_dic.txt','little_wome.txt']
#перебераем каждую книгу из списка
for filename in filenames:
    #вызываем функцию в скобках указываем каждый файл кники и передаем в параметр
    count_words(filename)
"""Подсчитать поличество слов переменной"""
# title = 'Alice in Wonderland'
# print(title.split())
# print(len(title.split()))

