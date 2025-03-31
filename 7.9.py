# -*- coding: utf-8 -*-
"""
7.9
"""
N, K, R = map(float, input("Введите N, K, R через пробел: ").split())
day = 1
while N < 2:
    N += N * (K / 100)
    day += 1
print(day)