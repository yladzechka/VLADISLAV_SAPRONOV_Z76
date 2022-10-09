def string_to_number():
    item = input("Введите число: ")

    if item.isdigit() == True and float(item) > 0:
        print(f"Вы ввели положительное целое число: {item}")
    elif item.replace('.', '', 1).isdigit() == True and float(item) > 0:
        print(f"Вы ввели положительное дробное число: {item}")
    elif item.lstrip('-').isdigit() == True and float(item) < 0:
        print(f"Вы ввели отрицательное целое число: {item}")
    elif item.replace('.', '', 1).lstrip('-').isdigit() == True and float(item) < 0:
        print(f"Вы ввели отрицательное дробное число: {item}")
    else:
        print(f"Вы ввели не корректное число: {item}")

string_to_number()