def cat_dog(filename):
    try:
        with open(filename) as file:
            catdog = file.read()
    except FileNotFoundError:
        pass
        # print(f'File {filename} is not')
    else:
        print(f'{filename}\n{catdog}\n')


filenames = ['cats.txt','Dogs.txt']
for filename in filenames:
    cat_dog(filename)

def text(book):
    try:
        with open(book) as b:
            bb = b.read()
    except FileNotFoundError:
        print(f' Book - {book} not found')
    else:
        #Подсчитывает количество 'the' в книге 
        print(f'"the" in {book} are "{bb.lower().count("the ")}"')

books = ['text_1.txt','text_2.txt']
for book in books:
    text(book)