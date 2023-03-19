# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self):
        self.lst.sort()
        return sorted(self.lst, reverse=False)


if __name__ == "__main__":
    sort_list = SomeClass()
    print(sort_list.sorted_func())
