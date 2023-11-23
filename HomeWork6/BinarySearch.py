class BinarySearch():

    def search_iterative(self, list, item):
        # low и high отслеживают, в какой части списка будем выполнять поиск.
        low = 0
        high = len(list) - 1

        # цикл While используется для сужения поиска до одного элемента.
        while low <= high:
            # ... проверяем средний элемент
            mid = (low + high) // 2
            guess = list[mid]
            # Если искомое значение равно среднему элементу, возвращаем ее индекс
            if guess == item:
                return mid
            # Если искомое значение больше среднего элемента.
            if guess > item:
                high = mid - 1
            # Если искомое значение меньше среднего элемента.
            else:
                low = mid + 1

        # Если искомое значение не существует, то возвращаем -1
        return -1

    def search_recursive(self, list, low, high, item):
        # Проверяем базовый вариант
        if high >= low:

            mid = (high + low) // 2
            guess = list[mid]

            # Если искомое значение равно среднему элементу, возвращаем ее индекс
            if guess == item:
                return mid

                # Если искомое значение меньше среднего элемента, то он может присутсвовать,
            # только в левом подмассиве.
            elif guess > item:
                return self.search_recursive(list, low, mid - 1, item)

                # Иначе, искомое значение может может присутсвовать, только в правом подмассиве.
            else:
                return self.search_recursive(list, mid + 1, high, item)

        else:
            # Элемент отсутствует в массиве, возвращает -1
            return -1


if __name__ == "__main__":
    # Инициализируем класс, чтобы использовать методы этого класса.
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3))  # => 1

    #  Используем '-1', чтобы указать, что элемент не был найден.
    print(bs.search_iterative(my_list, 6))  # => -1