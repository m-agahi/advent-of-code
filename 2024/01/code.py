import sys
from math import gcd
from time import sleep
import math

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
    dataset = readinput()
    dataset = convert_input(dataset)
    
    ans = part1(dataset)
    print(f"part 1: {ans}")

    ans = part2(dataset)
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        temp = [int(num) for num in line.split()]
        result.append(temp)
    return result

############################################################
def part1(dataset):
    leftlist = []
    rightlist = []
    
    for i in range(len(dataset)):
        num1, num2 = dataset[i]
        leftlist.append(num1)
        rightlist.append(num2)

    leftlist.sort()
    rightlist.sort()

    total_distance = 0
    for i in range(len(leftlist)):
        total_distance += abs(leftlist[i] - rightlist[i])

    return total_distance    

############################################################
def part2(dataset):
    leftlist = []
    rightlist = []
    
    for i in range(len(dataset)):
        num1, num2 = dataset[i]
        leftlist.append(num1)
        rightlist.append(num2)

    leftlist.sort()
    rightlist.sort()

    similiarity = 0
    for leftrow in leftlist:
        repeat = 0
        for rightrow in rightlist:
            if leftrow == rightrow:
                repeat += 1
        similiarity += leftrow*repeat
    return similiarity
############################################################
main()