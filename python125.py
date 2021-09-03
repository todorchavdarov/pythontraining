import os
import sys
import re


# path = input("Enter file path :")

path = "D:\pyfiles\\temperature.txt"
output_file = open("converted_temps.txt", "w")


def conversion_to_c(value):
    return ((value-32)*5.0)/9.0


def conversion_to_f(value):
    return 9.0/5.0 * value + 32


with open(path) as filename:
    for line in filename:

        if "C" in line:
            degree = float(line[:-2])
            converted = conversion_to_f(degree)
            output_file.write(str(converted)+'\n')
            # print(converted)
        elif "F" in line:
            degree = float(line[:-2])
            converted = conversion_to_c(degree)
            output_file.write(str(converted)+'\n')
            # print(converted)


output_file.close()
