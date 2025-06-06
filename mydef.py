#19
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print("Сумма чисел:", result)
#20
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  
print(is_prime(4))  
#21
def calculate_average(numbers):
    if not numbers:  
        return 0
    return sum(numbers) / len(numbers)
grades = [85, 90, 78, 92, 88]
average = calculate_average(grades)
print("Среднее значение:", average)  