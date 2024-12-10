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
    
    ans,endpoints_list = part1(copy.deepcopy(dataset_original))
    print(f"part 1: {ans}")
    
    ans = part2(copy.deepcopy(endpoints_list))
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    new_dataset = []
    for line in dataset:
        temp_row = []
        for i in range(len(line)):
            temp_row.append(int(line[i]))
        new_dataset.append(temp_row)
    
    return new_dataset

############################################################
def part1(dataset_p1):
    dataset = dataset_p1
    summary = 0
    # print(dataset)
    # print(empty_p1)
    start_points = detect_start_points(dataset)
    # print(start_points)
    endpoint = []
    for start_point in start_points:
        tempep = []
        tempep.append(trail_recursive(dataset, start_point[0], start_point[1],tempep))
        # print(tempep)
        endpoint.append(tempep[:-1])
    print(endpoint)
    # for line in endpoint:
    #     print(line)
    
    summary = get_unique_lengths(endpoint)
    return summary, endpoint

############################################################
def part2(dataset_p2):
    dataset = dataset_p2
    summary = 0
    for line in dataset:
        summary += len(line)
    
    return summary

############################################################
def detect_start_points(dataset):
    start_points = []
    for i in range(len(dataset)):
        for j in range(len(dataset[0])):
            if dataset[i][j] == 0:
                start_points.append([i, j])
    return start_points
############################################################
def trail_recursive(dataset, i, j, endpoint):
    # print(i, j)
    if i < 0 or i >= len(dataset) or j < 0 or j >= len(dataset[0]):
        return ([-1, -1])
    if dataset[i][j] == 9:
        return ([i, j])
    if i+1 < len(dataset):
        if dataset[i+1][j] == dataset[i][j] + 1:
            ep = trail_recursive(dataset, i+1, j, endpoint)
            if ep != [-1, -1]:
                endpoint.append(ep)
    if i-1 >= 0:
        if dataset[i-1][j] == dataset[i][j] + 1:
            ep = trail_recursive(dataset, i-1, j, endpoint)
            if ep != [-1, -1]:
                endpoint.append(ep)
    if j+1 < len(dataset[0]):
        if dataset[i][j+1] == dataset[i][j] + 1:
            ep = trail_recursive(dataset, i, j+1, endpoint)
            if ep != [-1, -1]:
                endpoint.append(ep)
    if j-1 >= 0:
        if dataset[i][j-1] == dataset[i][j] + 1:
            ep = trail_recursive(dataset, i, j-1, endpoint)
            if ep != [-1, -1]:
                endpoint.append(ep)
    return ([-1, -1])
    
############################################################
def get_unique_lengths(dataset):
    unique_lengths = []
    summary = 0
    for line in dataset:
        # Convert the list of lists into a set of tuples to remove duplicates
        unique_items = set(tuple(item) for item in line)
        unique_lengths.append(len(unique_items))
        summary += len(unique_items)

    return summary
############################################################
main()