import concurrent.futures
from functools import cache
import sys
import os
from math import gcd
from time import sleep
from time import time
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
    t1 = time()
    input_dataset = readinput()
    dataset_original = convert_input(copy.deepcopy(input_dataset))
    
    ans = part1(copy.deepcopy(dataset_original))
    print(f"part 1: {ans}")
    
    ans = sum(part2(x, 75) for x in copy.deepcopy(dataset_original))
    print(f"part 2: {ans}")
    t2 = time()
    t = round(t2-t1, 4)
    print(f"Time: {t} seconds")
############################################################
def convert_input(dataset):
    new_dataset = []
    for number in dataset[0].split(" "):
        new_dataset.append(int(number))
    
    return new_dataset

############################################################
def part1(dataset_p1):
    dataset = dataset_p1
    summary = 0

    for count in range(25):
        tempds =[]
        for i in range(len(dataset)):
            number = dataset[i]
            if number == 0:
                tempds.append(1)
            elif len(str(number)) % 2 == 0:
                left = int(str(number)[:len(str(number))//2])
                right = int(str(number)[len(str(number))//2:])
                tempds.append(left)
                tempds.append(right)
            else:
                tempds.append(number*2024)
        dataset = tempds
    summary = len(dataset)


    return summary
############################################################
# NOT MY SOLUTION :/
@cache
def part2(stone: int, depth: int) -> int:
    if depth == 0:
        return 1
    elif stone == 0:
        return part2(1, depth - 1)
    else:
        num_digits = math.floor(math.log10(stone)) + 1
        if num_digits % 2 == 0:
            d = 10 ** (num_digits // 2)
            return part2(stone // d, depth - 1) + part2(stone % d, depth - 1)
        else:
            return part2(stone * 2024, depth - 1)
############################################################
main()