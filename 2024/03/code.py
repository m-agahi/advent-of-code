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
    dataset = convert_input(dataset)
    
    ans = part1(dataset)
    print(f"part 1: {ans}")

    ans = part2(dataset)
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    result= []
    for item in dataset:
        result.append(item)
    return result

############################################################
def part1(dataset):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    summary = 0
    for item in dataset:
        matches = [(int(num1), int(num2)) for num1, num2 in find_all_p1(pattern,item)]
        summary += mult(matches)
    return summary

############################################################
def part2(dataset):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    matches = []
    summary = 0
    for item in dataset:
        matches.append(extract_matches_with_indexes(pattern,item))
    enabled = True
    for item in matches:
        for match in item:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            else:
                if enabled:
                    num1 = int(match.split(",")[0].split("(")[1])
                    num2 = int(match.split(",")[1].split(")")[0])
                    summary += num1 * num2
    return summary
############################################################
def find_all_p1(pattern,dataset):
    matches = re.findall(pattern, dataset)
    return matches
############################################################
def extract_matches_with_indexes(pattern,input_string):
    matches = [(match.group()) for match in re.finditer(pattern, input_string)]
    return matches
############################################################
def mult(dataset):
    summary = 0
    for item in dataset:
        summary += item[0] * item[1]
    return summary
############################################################
main()