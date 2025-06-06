#16
student = {
    "имя": "Анна",
    "возраст": 20,
    "курс": 3
}
print("Информация о студенте:")
for key, value in student.items():
    print(f"{key}: {value}")
#17
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Объединенный словарь:", merged_dict)
#18
my_dict = {"apple": "яблоко", "banana": "банан", "orange": "апельсин"}
key_to_check = "banana"
if key_to_check in my_dict:
    print(f"Ключ '{key_to_check}' присутствует в словаре")
else:
    print(f"Ключ '{key_to_check}' отсутствует в словаре")