# -*- coding: utf-8 -*-
"""
7.1
"""
count = 0
numbers = []
for i in range(100, 1000):
    if i % 17 == 0:
        numbers.append(i)
        count += 1
        
print(" ".join(map(str, numbers)))
print(count)