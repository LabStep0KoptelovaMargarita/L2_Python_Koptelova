num = int(input("Введите целое число: "))
if num % 2 == 0:
    print(f"{num} - четное число")
else:
    print(f"{num} - нечетное число")
if num1 > num2:
    print("Наибольшее число:", num1)
elif num2 > num1:
    print("Наибольшее число:", num2)
else:
    print("Числа равны")
age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вы можете получить водительские права!")
else:
    print("Вы пока не можете получить водительские права.")
    print(f"До прав осталось {18 - age} лет")