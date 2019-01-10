#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique

path = "C:/learning/data_light_cp1251.json"

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(Unique(sorted(list(field(arg, "job-name"))), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + "с опытом Python", arg))

@print_result
def f4(arg):
    salaries = list(gen_random(100000, 200000, len(list(arg))))
    return list(zip(list(arg), list(map(lambda x: "зарплата " + str(x) + " руб.", salaries))))

with timer():
    f4(f3(f2(f1(data))))