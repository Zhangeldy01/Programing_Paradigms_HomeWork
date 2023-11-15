# Задача №2
# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру
# для сортировки числа в списке в порядке убывания.

 # Declarative programming paradigm
numbers = [8, 12, 6, 21, 15, 3, 9, 0]
def sort_list(numbers):
    return sorted(numbers, reverse=True)
print("Отсортированный список:", sort_list(numbers))