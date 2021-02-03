from itertools import count
from itertools import cycle

a = int(input("Введите с какого числа начинать вывод целых чисел: "))
new_list1 = []
for element in count(a):
    if element > 25:
        break
    else:
        new_list1.append(element)
print(new_list1)



new_list2 = ["ABCDEFG", 21324, 12.13124, True,]
k = cycle(new_list2)
a = int(input("Введите число поовторений вывода элементов списка: "))
for i in (x for _ in range(a) for x in new_list2):
    print(next(k))


