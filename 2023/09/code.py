import sys
from math import gcd
from time import sleep
import math

############################################################
if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)
input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File not found or path is incorrect.")

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        numbers = []
        temp=line.split()
        for i in temp:
            numbers.append(int(i))
        result.append(numbers)
    return result

############################################################
def differences(dataset):
    result = []
    for i in range(len(dataset)-1):
        diff = dataset[i+1] - dataset[i]
        result.append(diff)
    return result

############################################################
def check_all_zeros(dataset):
    result = True
    for i in dataset:
        if i !=0:
            result=False
            break
    return result
############################################################
def extrapolate_next(dataset,diffs):
    result = dataset[-1]
    summary = 0
    for i in range(len(diffs)-2,-1,-1):
        summary += diffs[i][-1]
    result += summary
    return result

############################################################
def part1(dataset):
    summary=0
    for line in dataset:
        diffs = []
        diffs.append(differences(line))
        zero = check_all_zeros(diffs[-1])
        while not zero:
            diffs.append(differences(diffs[-1]))
            zero = check_all_zeros(diffs[-1])
        ext = extrapolate_next(line,diffs)
        summary += ext
    return summary

############################################################
def extrapolate_previous(dataset,diffs):
    result = dataset[0]
    summary = diffs[-2][0]
    for i in range(len(diffs)-2,0,-1):
        summary = diffs[i-1][0] - summary
    
    result -= summary
    return result

############################################################
def part2(dataset):
    summary=0
    for line in dataset:
        diffs = []
        diffs.append(differences(line))
        zero = check_all_zeros(diffs[-1])
        while not zero:
            diffs.append(differences(diffs[-1]))
            zero = check_all_zeros(diffs[-1])
        ext = extrapolate_previous(line,diffs)
        summary += ext
    
    return summary

############################################################
############################################################

dataset = convert_input(input)
ans = part1(dataset)
print(f"part 1: {ans}")
ans = part2(dataset)
print(f"part 2: {ans}")
