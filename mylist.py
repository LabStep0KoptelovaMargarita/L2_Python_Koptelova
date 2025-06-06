#13
numbers = [3, 7, 2, 9, 5]
total = sum(numbers)
print("Сумма чисел в списке:", total)
#14
numbers = [4, 12, 7, 23, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Максимальное число (с циклом):", max_num)
#15
original_list = [2, 5, 2, 7, 5, 8, 2]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print("Без дубликатов (с сохранением порядка):", unique_list)