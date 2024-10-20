import re
from itertools import combinations, permutations

print("======\n"
      "Вводится трехзначное число из разных цифр.\n"
      "======")

while True:
    num = input("Введите число: ")
    if num == "exit":
        print("Exit...")
        break
    elif len(num) > 3:
        print("Длина введенного числа больше 3!")
    elif len(num) < 3:
        print("Длина введенного числа меньше 3!")
    elif not num.isdecimal():
        print("Введено не число или формат введенного числа не верен!")
    elif len(set(num)) != 3:
        print("В введенном числе встречаются повторяющиеся цифры!")
    elif re.match(r"^[0-9]{3}$", num):
        p = ', '.join(''.join(permutation) for permutation in permutations(num))
        print(f"шесть чисел, образованных при перестановке цифр заданного числа:\n{p}")
    else:
        print("Не верный формат числа!")
