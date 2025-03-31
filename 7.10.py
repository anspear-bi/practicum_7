# -*- coding: utf-8 -*-
"""
7.10
"""

previous_temperature = None
decrease_count = 0

while True:
    current_temperature = float(input("Введите температуру: "))
    if current_temperature == 0:
        break
    if previous_temperature is not None and current_temperature < previous_temperature:
        decrease_count += 1
    previous_temperature = current_temperature
print(decrease_count)
