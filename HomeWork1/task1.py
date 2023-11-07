# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру
# для сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

# Imperative programming paradigm
# Selection Sort (сортировка выбором)
arr = [8, 12, 6, 21, 15, 3, 9, 0]
def selection_sort(arr):
    for i in range(len(arr)):
        maximum = i
        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] > arr[maximum]:
                maximum = j
        # Помещаем это перед отсортированным концом массива
        arr[maximum], arr[i] = arr[i], arr[maximum]
    return arr
print("Отсортированный список:", selection_sort(arr))