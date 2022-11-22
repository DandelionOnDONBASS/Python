print("1")
name = "ada lovelace"
print(name.title())      # 1

print("2")
name = "Ada Lovelace"
print(name.upper())
print(name.lower())        #2

print("3")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)                                #3

print("4")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}")         #4

print("4")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello {full_name.title()}"
print(message)                                      #5


print("5")
full_name = "{} {}".format(first_name, last_name)     #6
print("6")
print("\tPython")                   #7
print("7")
print("Languages: \n\tPhyton\n\tC\n\tJavaScript")     #7
print("8")
favorite_language = " python "
favorite_language = favorite_language.rstrip()          #8 удаление пробела в конце строки
favorite_language= favorite_language.lstrip()
print(favorite_language)




