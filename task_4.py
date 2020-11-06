"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections, timeit

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)


def dict_get():
    return my_dict.get('a')


def dict_keys():
    return list(my_dict.keys())


def dict_append():
    my_dict['d'] = 4
    return my_dict


# def dict_popitem():
#     return my_dict.popitem()


print(timeit.timeit("dict_get()", setup="from __main__ import dict_get"))
print(timeit.timeit("dict_keys()", setup="from __main__ import dict_keys"))
print(timeit.timeit("dict_append()", setup="from __main__ import dict_append"))
# print(timeit.timeit("dict_popitem()", setup="from __main__ import dict_popitem"))

my_odict = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(my_odict)


def odict_get():
    return my_odict.get('a')


def odict_keys():
    return list(my_odict.keys())


def odict_append():
    my_odict['d'] = 4
    return my_odict

#
# def odict_popitem():
#     return my_odict.popitem()


print(timeit.timeit("dict_get()", setup="from __main__ import dict_get"))
print(timeit.timeit("dict_keys()", setup="from __main__ import dict_keys"))
print(timeit.timeit("dict_append()", setup="from __main__ import dict_append"))
# print(timeit.timeit("dict_popitem()", setup="from __main__ import dict_popitem"))


"""Замеры показали практически одинакове значения, что свидетельствует о том, что нет большой необходимости
импортировать OrderDict, так как уже встроенные Dict справляются со своей задачей полностью"""