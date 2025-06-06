#25
while True:
    try:
        num = float(input("Введите число: "))
        print(f"Вы ввели число: {num}")
        break 
    except ValueError:
        print("Ошибка! Введено не число. Попробуйте снова.")
#26
filename = input("Введите имя файла: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден!")
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")