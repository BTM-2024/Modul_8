# Задача "План перехват"
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for namber in numbers:
        try:
            result += namber
        except  TypeError:
            print(f'некорректный тип данных для подсчета суммы-',numbers)
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result, incorrect_data= personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    correct_len = len(numbers) - incorrect_data

    try:
        avg = result / correct_len
    except ZeroDivisionError:
        return 0

    return avg

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать