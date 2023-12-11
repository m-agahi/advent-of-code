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
    return 

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        temp=[]
        for i in range(len(line)):
            char = line[i]
            if char == ".":
                temp.append(1)
            else:
                temp.append(-1)
        result.append(temp)
    return result

############################################################
def part1(dataset):
    expanded = []
    hs = []
    vs = []
    hs,vs = detect_empty(dataset)
    expanded = expand(dataset,hs,vs,2)
    sum_distancd= calculate(expanded)
    return sum_distancd

############################################################
def detect_empty(dataset):
    hs = []
    vs = []
    # rows
    for i in range(len(dataset)):
        empty = True
        for char in dataset[i]:
            if char == -1: 
                empty = False
                break
        hs.append(empty)
    # columns
    for j in range(len(dataset[0])):
        empty = True
        for i in range(len(dataset)):
            char = dataset[i][j]
            if char == -1:
                empty = False
                break
        vs.append(empty)
    return hs,vs

############################################################
def expand (dataset,hs,vs,oldness):
    expanded = []
    empty_row = []
    cols = 0
    for col in vs:
        if col: cols +=1
    for i in range(len(hs)):
        empty_row.append(oldness)

    temp = []
    for i in range(len(hs)):
        if not hs[i]:
            temp.append(dataset[i])
        else:
            temp.append(empty_row)
            # temp.append(dataset[i])

    for i in range(len(temp)):
        t = []
        for j in range(len(temp[0])):
            char = temp[i][j]
            if not vs[j]:
                t.append(char)
            else:
                t.append(oldness)
                # t.append(char)
        expanded.append(t)
    # for line in expanded: print(line)
    return expanded

############################################################
def calculate(dataset):
    summary = 0
    galaxies = []
    for row in range(len(dataset)):
        for col in range(len(dataset[0])): 
            char = dataset[row][col]
            if char == -1:
                galaxies.append([row,col])
    for i in range(len(galaxies)-1):
        for j in range(i+1,(len(galaxies))):
            g1r = galaxies[i][0] 
            g1c = galaxies[i][1] 
            g2r = galaxies[j][0] 
            g2c = galaxies[j][1] 
            
            sumr = 0
            rowadd = 1
            if g1r == len(dataset): rowadd = 0
            for row in range(g1r+rowadd,g2r+1):
                sumr += abs(dataset[row][g1c])

            sumc = 0
            cols = g1c
            cole = g2c
            if g1c > g2c : 
                cols = g2c
                cole = g1c
            coladd = 1
            if cols == len(dataset[0]): coladd = 0
            for col in range(cols+coladd,cole+1):
                sumc += abs(dataset[g1r][col])
            distance = sumc+sumr
            # print(galaxies[i],galaxies[j],distance)
            summary += distance    
    return summary

############################################################
def part2(dataset):
    expanded = []
    hs = []
    vs = []
    hs,vs = detect_empty(dataset)
    expanded = expand(dataset,hs,vs,1000000)
    sum_distancd= calculate(expanded)
    for line in expanded: print(line)
    return sum_distancd
############################################################
main()