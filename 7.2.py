# -*- coding: utf-8 -*-
"""
7.2
"""
input_string = input("Введите строку: ")
output_string = ""
for i in range(len(input_string)):
    if (i + 1) % 3 == 0:
        output_string += input_string[i]
print(output_string)
   