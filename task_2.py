"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict
from functools import reduce

my_dict = defaultdict(list)
print(my_dict)

a = list("A2")
for i in range(len(a)):
    my_dict[1].append(a[i])

b = list("C4F")
for i in range(len(b)):
    my_dict[2].append(b[i])

print(my_dict)

my_list = []
my_list.append(int("".join(my_dict[1]), 16))
my_list.append(int("".join(my_dict[2]), 16))

my_sum = list(hex(reduce(lambda x, y: x + y, my_list))[2:].upper())
for i in range(len(my_sum)):
    my_dict["sum"].append(my_sum[i])

my_mul = list(hex(reduce(lambda x, y: x * y, my_list))[2:].upper())
for i in range(len(my_mul)):
    my_dict["mul"].append(my_mul[i])

print(my_dict)

# print(f"Сумма чисел {my_dict[1]} и {my_dict[2]} равна {my_sum}")
# print(f"Произведение чисел {my_dict[1]} и {my_dict[2]} равна {my_mul}")
