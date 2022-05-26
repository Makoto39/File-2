def check_input(input_string):
    if len(input_string) == 0:
        print("Вы ввели пустую строку.")
        return False
    for i in input_string:
        if not i.isnumeric():
            print("Необходимо вводить только числовые значения")
            return False
    return True


def sort_bubble(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


def search_binare(array, value):
    mid = len(array) // 2
    low = 0
    high = len(array) - 1
    while array[mid] != value and low <= high:
        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("Значение не найдено")
    else:
        print("Значение найдено. Индекс значения =", mid)


while (True):
    input_string = input("Введите числа в одну строку через пробел.\n").split()
    if check_input(input_string):
        break

input_int = [int(i) for i in input_string]
sorted_input_int = sort_bubble(input_int)

while (True):
    desired_value = input("Введите значение искомого элемента!\n").split()
    if check_input(desired_value):
        desired_value = int(desired_value[0])
        break

search_binare(sorted_input_int, desired_value)