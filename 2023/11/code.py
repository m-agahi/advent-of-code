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
    # dataset = convert_input(input)
    ans = part1(dataset)
    # for line in dataset: 
    #     print(line)
    #     for char in line:
    #         print(char,end='')
    #     print("")
    print(f"part 1: {ans}")
    # ans = part2()
    # print(f"part 2: {ans}")


    return

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        temp=[]
        for i in range(len(line)):
            temp.append(line[i])
        result.append(temp)
    return result

############################################################
def part1(dataset):
    hs = []
    vs = []
    expanded = []
    # rows
    for i in range(len(dataset)):
        empty = True
        for char in dataset[i]:
            if char == "#": 
                empty = False
                break
        hs.append(empty)
    # columns
    for j in range(len(dataset[0])):
        empty = True
        for i in range(len(dataset)):
            char = dataset[i][j]
            if char == "#":
                empty = False
                break
        vs.append(empty)
    expanded = expand(dataset,hs,vs)
    sum_distancd= calculate(expanded)
    return sum_distancd

############################################################
def expand (dataset,hs,vs):
    expanded = []
    empty_row = []
    cols = 0
    for col in vs:
        if col: cols +=1
    for i in range(len(hs)):
        empty_row.append(".")
    temp = []
    for i in range(len(hs)):
        if not hs[i]:
            temp.append(dataset[i])
        else:
            temp.append(empty_row)
            temp.append(dataset[i])
    for i in range(len(temp)):
        t = []
        for j in range(len(temp[0])):
            char = temp[i][j]
            if not vs[j]:
                t.append(char)
            else:
                t.append(".")
                t.append(char)
        expanded.append(t)
    return expanded

############################################################
def calculate(dataset):
    summary = 0
    galaxies = []
    for i in range(len(dataset)):
        for j in range(len(dataset[0])): 
            char = dataset[i][j]
            if char == "#":
                galaxies.append([i,j])
    for i in range(len(galaxies)-1):
        for j in range(i+1,(len(galaxies))):
            g1x = galaxies[i][0] 
            g1y = galaxies[i][1] 
            g2x = galaxies[j][0] 
            g2y = galaxies[j][1] 
            
            distance = abs(g2x-g1x) + abs(g2y-g1y)
            # print(galaxies[i],galaxies[j],distance)
            summary += distance    
    # print(summary)
    return summary

############################################################
def part2():
    
    return 

############################################################
main()