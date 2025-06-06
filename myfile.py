#22
with open("example.txt", "w") as file:
    file.write("Hello, File!")
print("Файл создан и в него записана строка")
#23
with open("example.txt", "r") as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)
with open("example.txt", "a") as file:
    file.write("\nThis is a new line!")
#24
with open("example.txt", "r") as file:
    print("\nОбновленное содержимое файла:")
    print(file.read())