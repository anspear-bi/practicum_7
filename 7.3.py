# -*- coding: utf-8 -*-
"""
7.3
"""
import math

while True:
    number = int(input("Введите число: "))
    if math.isqrt(number) * 2 == number:  
        print(f"{number} является полным квадратом.")
        break
    else:
        print(f"{number} не является полным квадратом.")
