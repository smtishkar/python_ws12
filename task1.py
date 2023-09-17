# Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k значений.
#  Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.


class MyFac:
    def __init__(self, size: int):
        self._size = size
        self.__archiv: list = []

    def show_archiv(self):
        return self.__archiv

    def __call__(self, namber: int):
        res: int = 1
        for i in range(1, namber+1):
            res *= i

        if len(self.__archiv) >= self._size:
            self.__archiv.pop(0)
        self.__archiv.append({namber: res})
        return res


if __name__ == '__main__':
    f1 = MyFac(size=4)
    print(f1(1))
    print(f1(2))
    print(f1(3))
    print(f1(4))
    print(f1(5))
    print(f1(6))
    print(f1(7))
    print(f1.show_archiv())