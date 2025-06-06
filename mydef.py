def add_numbers(a, b):
    return a + b

# Пример использования
result = add_numbers(5, 3)
print("Сумма чисел:", result)  # Вывод: 8
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Пример использования
print(is_prime(7))  # Вывод: True
print(is_prime(4))  # Вывод: False
def calculate_average(numbers):
    if not numbers:  # Проверка пустого списка
        return 0
    return sum(numbers) / len(numbers)

# Пример использования
grades = [85, 90, 78, 92, 88]
average = calculate_average(grades)
print("Среднее значение:", average)  # Вывод: 86.6