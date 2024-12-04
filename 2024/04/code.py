import sys
from math import gcd
from time import sleep
import math
import re

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
    # dataset = convert_input(dataset)
    
    ans = part1(dataset)
    print(f"part 1: {ans}")

    ans = part2(dataset)
    print(f"part 2: {ans}")

############################################################
# def convert_input(dataset):
#     result= []
#     for line in dataset:
#         temp = [int(num) for num in line.split()]
#         result.append(temp)
#     return result

############################################################
def part1(dataset):
    summary = 0
    transposed = [''.join(row) for row in zip(*dataset)]
    
    pattern1 = r"XMAS"
    pattern2 = r"SAMX"
    
    for pattern in [pattern1, pattern2]:
        for item in dataset:
            matches = re.findall(pattern, item)
            summary += len(matches)
    for pattern in [pattern1, pattern2]:
        for item in transposed:
            matches = re.findall(pattern, item)
            summary += len(matches)
    diagonallr, diagonalrl = extract_diagonals(dataset)

    for pattern in [pattern1, pattern2]:
        for item in diagonallr:
            matches = re.findall(pattern, item)
            summary += len(matches)
    for pattern in [pattern1, pattern2]:
        for item in diagonalrl:
            matches = re.findall(pattern, item)
            summary += len(matches)


    return summary

############################################################
def part2(dataset):
    lines = len(dataset)
    cols = len(dataset[0])
    summary = 0
    pattern1 = r"MAS"
    pattern2 = r"SAM"

    for i in range(1,lines-1):
        for j in range(1,cols-1):
            if dataset[i][j] == "A":
                lr = dataset[i-1][j-1] + dataset[i][j] + dataset[i+1][j+1]
                rl = dataset[i-1][j+1] + dataset[i][j] + dataset[i+1][j-1]
                m1 = len(re.findall(pattern1, lr))
                m2 = len(re.findall(pattern2, lr))
                m3 = len(re.findall(pattern1, rl))
                m4 = len(re.findall(pattern2, rl))
                if m1+m2+m3+m4 == 2:
                    summary += 1

    return summary
############################################################
def findthemall(dataset):
    for i in range(len(dataset)):
        for j in range(i+1, len(dataset)):
            for k in range(j+1, len(dataset)):
                if dataset[i] + dataset[j] + dataset[k] == 2020:
                    return dataset[i], dataset[j], dataset[k]
    return
############################################################
def extract_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    diagonals_tl_br = []
    diagonals_tr_bl = []

    for start_row in range(rows):
        diagonal = []
        r, c = start_row, 0
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonals_tl_br.append("".join(diagonal))

    for start_col in range(1, cols):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c < cols:
            diagonal.append(grid[r][c])
            r += 1
            c += 1
        diagonals_tl_br.append("".join(diagonal))

    for start_row in range(rows):
        diagonal = []
        r, c = start_row, cols - 1
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonals_tr_bl.append("".join(diagonal))

    for start_col in range(cols - 2, -1, -1):
        diagonal = []
        r, c = 0, start_col
        while r < rows and c >= 0:
            diagonal.append(grid[r][c])
            r += 1
            c -= 1
        diagonals_tr_bl.append("".join(diagonal))

    return diagonals_tl_br, diagonals_tr_bl

############################################################
main()