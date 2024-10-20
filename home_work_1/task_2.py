print("======\n"
      "Вводится целое положительное число.\n"
      "======")

while True:
    num = input("Введите число: ")

    if num == "exit":
        print("Exit...")
        break

    num = int(num)
    minus_num, num_plus_one = -num, num + 1
    sum_minus = 0 # sum(range(minus_num, 0))
    sum_plus = 0 # sum(range(0, num_plus_one + 1))

    # print(f"Все числа в интервале [-число; число+1]: {list(range(minus_num, num_plus_one + 1))}")

    print(f"Все числа в интервале [-число; число+1] = [{minus_num}, {num_plus_one}]:")
    all_nums = []
    for n in range(minus_num, num_plus_one + 1):
        all_nums.append(str(n))
        if n < 0:
            sum_minus += n
        else:
            sum_plus += n
    print(', '.join(all_nums))

    print(f"Сумма отрицательных чисел: {sum_minus}")
    print(f"Сумма положительных чисел: {sum_plus}")
