# Структурная парадигма
n = int(input())
for i in range(1, n + 1):
    print(str(i) + "--------")
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)

"""Выбор структурной парадигмы обосновывается тем, что задача простая и для ее решения используется цикл for. 
Процедурная парадигма для больших программ, где нужна модульность и переиспользование кода.
"""
