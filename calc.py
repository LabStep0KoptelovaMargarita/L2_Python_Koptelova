#30
def calculate():
    while True:
        try:
            expression = input("Введите выражение (например, 2 + 2): ").split()
            if len(expression) != 3:
                print("Ошибка! Используйте формат: число оператор число")
                continue
            a = float(expression[0])
            operator = expression[1]
            b = float(expression[2])
            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a / b
            else:
                print("Ошибка: неверный оператор! Используйте +, -, * или /")
                continue
            print(f"Результат: {result}")
            break
            
        except ValueError:
            print("Ошибка: введите числа корректно!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
if __name__ == "__main__":
    calculate()