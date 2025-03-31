# -*- coding: utf-8 -*-
"""
7.5
"""
N = int(input("Введите значение N: "))
volumes = []
i = 1
while True:
    volume = i * 3
    if volume > N:
        break
    volumes.append(volume)
    i += 1
print(" ".join(map(str, volumes)))
