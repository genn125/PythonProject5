# 5.3
# Задача "Нужно больше этажей":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self): # 1 ,2
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other): # 3
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): # 10
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other): # 11
                return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): # 8
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): # 9
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other): # 12
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value): # 4, 5
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value): # 6
        return self.__add__(value)

    def __radd__(self, value): # 7
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print('1 __str__', h1)
print('2 __str__', h2)

print('3 (__eq__)', h1 == h2)

h1 += 10 # __add__
print('4 (__add__)', h1)
print('5 (__add__)', h1 == h2)

h1 += 10 # __iadd__
print('6 (__iadd__)', h1)

h2 = 10 + h2 # __radd__
print('7 (__radd__)', h2)

print('8 __gt__', h1 > h2)
print('9 __ge__', h1 >= h2)
print('10 __lt__', h1 < h2)
print('11 __le__', h1 <= h2)
print('12 __ne__', h1 != h2)


