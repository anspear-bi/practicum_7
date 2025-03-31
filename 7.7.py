# -*- coding: utf-8 -*-
"""
7.7
"""

answer = int(input("Введите ваш ответ: "))
is_correct = False
for i in range(1, 11):  
    if 2 * i == answer:
        is_correct = True
        break
print("верно" if is_correct else "неверно")
