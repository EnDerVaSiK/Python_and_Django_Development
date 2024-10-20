import re

print("======\n"
      "Числа:\n"
      "- число может начинаться на '+' или '-', не является обязательным;\n"
      "- в целой части обязательно должна быть хотя бы одна цифра;\n"
      "- в целой части не может начинаться на '0' (исключение - единственный '0' в целой части);\n"
      "- десятичная часть не является обязательной;\n"
      "- перед десятичной частью ставится '.' (точка);\n"
      "- в десятичной части на конце не может быть '0'.\n"
      "В рамках этой задачи все остальное не является числом.\n"
      "Для выхода из программы введите 'exit'.\n"
      "======")


while True:
    num = input("Введите число: ")
    if num == "exit":
        print("Exit...")
        break
    if re.match("^[+-]?([1-9][0-9]*|0)([.][0-9]*[1-9])?$", num):
        print("Введено число! Его длина: "
              f"{len(re.findall("[0-9]", num))}")
    else:
        print("Несоответствие типа данных")
