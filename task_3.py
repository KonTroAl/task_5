"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import timeit

my_lst = list("bcde")

my_deq = deque(my_lst)
print(my_deq)


def deq_append():
    my_deq.append('f')
    return my_deq


def deq_appendleft():
    my_deq.appendleft('a')
    return my_deq


def deq_pop():
    my_deq.pop()
    return my_deq


def deq_popleft():
    my_deq.popleft()
    return my_deq

###########################################################

def lst_append():
    my_lst.append('f')
    return my_lst


def lst_insert():
    my_lst.insert(0, 'a')
    return my_lst


def lst_pop():
    my_lst.pop()
    return my_lst


def lst_popleft():
    my_lst.pop(0)
    return my_lst


print(timeit.timeit("deq_append()", setup="from __main__ import deq_append", number=10000))
print(timeit.timeit("deq_appendleft()", setup="from __main__ import deq_appendleft", number=10000))
print(timeit.timeit("deq_pop()", setup="from __main__ import deq_pop", number=10000))
print(timeit.timeit("deq_popleft()", setup="from __main__ import deq_popleft", number=10000))

print(my_lst)

print(timeit.timeit("lst_append()", setup="from __main__ import lst_append", number=10000))
print(timeit.timeit("lst_insert()", setup="from __main__ import lst_insert", number=10000))
print(timeit.timeit("lst_pop()", setup="from __main__ import lst_pop", number=10000))
print(timeit.timeit("lst_popleft()", setup="from __main__ import lst_popleft", number=10000))

"""Как показал замер, для ускорения операций по вставке элемента в очередь(список) лучше использовать deque, 
как и для получения элемента из очереди(списка), что соответсвует информации в документации"""
