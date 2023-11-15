from random import randint


def bubble_sort(array, direction):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if (direction == '<' and array[j] > array[j + 1]) or (direction == '>' and array[j] < array[j + 1]):
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))

print(a)

sorting_direction = input("Введите направление сортировки ('<' для возрастания, '>' для убывания): ")

bubble_sort(a, sorting_direction)

print(a)