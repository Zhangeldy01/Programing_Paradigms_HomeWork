'''Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.'''


def pearson_correlation(a1, b1):
    n = len(a1)  # длина массива
    # метод вычисляет среднее арифметическое элементов в массивах
    average_a1 = sum(a1) / n
    average_b1 = sum(b1) / n

    # Вычисление числителя
    numerator = 0.0
    for i in range(n):
        numerator += (a1[i] - average_a1) * (b1[i] - average_b1)

    # Вычисление знаменателя
    denominator_a1 = (sum((i - average_a1) ** 2 for i in a1) / n) ** 0.5
    denominator_b1 = (sum((i - average_b1) ** 2 for i in b1) / n) ** 0.5
    denominator = denominator_a1 * denominator_b1

    return numerator / denominator


# Пример
a1 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
b1 = [0.3, 0.6, 0.5, 0.7, 0.2, 0.9]

result = pearson_correlation(a1, b1)
print("Корреляция Пирсона: " + str(result))
