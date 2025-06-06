#31
import random

def guess_number():
    secret_number = random.randint(0, 10)
    attempts = 3
    
    print("Я загадал число от 0 до 10. У тебя 3 попытки, чтобы угадать его!")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Введи число: "))
            if guess == secret_number:
                print(f"Поздравляю! Ты угадал число {secret_number}!")
                return
            elif guess < secret_number:
                print("Не верно! Загаданное число больше!")
            else:
                print("Не верно! Загаданное число меньше!")
        except ValueError:
            print("Ошибка! Введи целое число.")
    print(f"\nК сожалению, попытки закончились. Загаданное число было: {secret_number}")
if __name__ == "__main__":
    guess_number()