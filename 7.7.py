# -*- coding: utf-8 -*-
"""
7.7
"""

answer = int(input("Введите ваш ответ: "))
is_correct = False
for i in range(1, 11):  # Предположим, что мы можем проверить от 1 до 10
    if 2 * i == answer:
        is_correct = True
        break
print("верно" if is_correct else "неверно")