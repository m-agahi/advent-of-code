import sys
import os
from math import gcd
from time import sleep
import math
import re
import copy

############################################################
def readinput():
    if len(sys.argv) != 2:
        print("Usage: python code.py input_filename")
        sys.exit(1)
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            dataset = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    return dataset

############################################################
def main():
    input_dataset = readinput()
    dataset_original = convert_input(copy.deepcopy(input_dataset))
    
    ans = part1(copy.deepcopy(dataset_original))
    print(f"part 1: {ans}")
    
    ans = part2(copy.deepcopy(dataset_original))
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    temp_row = []
    new_dataset = []
    
    for line in dataset:
        result=(int(line.split(":")[0]))
        temp_row.append(result)
        temp_row.append([int(number) for number in line.split(": ")[1].split(" ")])
        new_dataset.append(temp_row)
        temp_row = []

    return new_dataset

############################################################
def part1(dataset_p1):
    dataset = dataset_p1
    summary = 0
    for equation in dataset:
        if check_equation(equation):
            summary += equation[0]
    
    return summary

############################################################
def part2(dataset_p2):
    dataset = dataset_p2
    summary = 0
    for equation in dataset:
        if check_equation_p2(equation):
            summary += equation[0]

    return summary

############################################################
def check_equation(equation):
    possibilities = 2 ** (len(equation[1]) - 1)
    result_tree = [0] * possibilities
    for i in range(possibilities):
        current_result = equation[1][0]
        binary_pattern = bin(i)[2:].zfill(len(equation[1]) - 1)  
        
        for j in range(len(binary_pattern)):
            operator = "+" if binary_pattern[j] == "0" else "*"
            if operator == "+":
                current_result += equation[1][j + 1]
            else:
                current_result *= equation[1][j + 1]
        result_tree[i] = current_result
    for item in result_tree:
        if item == equation[0]:
            return True
    return False
############################################################
def check_equation_p2(equation):
    possibilities = 3 ** (len(equation[1]) - 1)
    result_tree = [0] * possibilities  

    for i in range(possibilities):
        current_result = equation[1][0]
        ternary_pattern = base_n(i, 3, len(equation[1]) - 1) 

        for j in range(len(ternary_pattern)):
            operator = ternary_pattern[j]
            if operator == "0":  # +
                current_result += equation[1][j + 1]
            elif operator == "1":  # *
                current_result *= equation[1][j + 1]
            elif operator == "2":  # ||
                current_result = int(str(current_result) + str(equation[1][j + 1]))
        result_tree[i] = current_result

    for item in result_tree:
        if item == equation[0]:
            return True
    return False

############################################################
def base_n(num, base, length):
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    while len(digits) < length:
        digits.append("0")
    return "".join(reversed(digits))
############################################################
main()