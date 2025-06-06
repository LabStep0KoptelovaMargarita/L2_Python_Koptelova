for i in range(1, 11):
    print(i)
n = int(input("Введите число N: "))
for number in range(1, n + 1):
    print(number)
total = 0
counter = 1
while counter <= 100:
    total += counter
    counter += 1
print("Сумма чисел от 1 до 100:", total)