# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint as r

def shuffle(A):
    last_index = len(A) - 1
    while last_index > 0:
        rand_index = r(0, last_index)
        A[last_index], A[rand_index] = A[rand_index], A[last_index]
        last_index -= 1
    return A

my_list = []
for i in range(10):
    my_list.append(r(0, 100))

print(f'Список до перемешивания: {my_list}')
print(f'Список после перемешивания: {shuffle(my_list)}')
