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
    new_dataset = []
    
    for line in dataset:
        temp_row = []
        for char in line:
            temp_row.append(char)
        new_dataset.append(temp_row)

    return new_dataset

############################################################
def part1(dataset_p1):
    dataset = dataset_p1
    summary = 0
    antena_locations = antena_location_finder(dataset)
    antinode_locations = []

    for i in range(len(antena_locations)-1):
        for j in range(i+1, len(antena_locations)):
            if antena_locations[i][0] == antena_locations[j][0]:
                location1,location2 = calculate_antinode(antena_locations[i], antena_locations[j])
                if location1[0] >= 0 and location1[0]<len(dataset) and location1[1]>=0 and location1[1]<len(dataset[0]):
                    antinode_locations.append(location1)
                if location2[0] >= 0 and location2[0]<len(dataset) and location2[1]>=0 and location2[1]<len(dataset[0]):
                    antinode_locations.append(location2)

    summary = len(set(tuple(item) for item in antinode_locations))        

    return summary

############################################################
def part2(dataset_p2):
    dataset = dataset_p2
    summary = 0
    antena_locations = antena_location_finder(dataset)
    antinode_locations = []

    for i in range(len(antena_locations)-1):
        for j in range(i+1, len(antena_locations)):
            if antena_locations[i][0] == antena_locations[j][0]:
                antinode_locations.append(calculate_antinode2(antena_locations[i], antena_locations[j],len(dataset),len(dataset[0])))
            
    summary = len(set(tuple(item) for sublist in antinode_locations for item in sublist))
    return summary

############################################################
def antena_location_finder(dataset):
    al = []
    for line in dataset:
        for char in line:
            if char == '.':
                continue
            else:
                al.append((char,dataset.index(line), line.index(char)))
    return al
############################################################
def calculate_antinode(antena1, antena2):
    diffx = abs(antena2[1] - antena1[1])
    diffy = antena2[2] - antena1[2]
    location1x = antena1[1]-diffx
    location1y = antena1[2]-diffy
    location2x = antena2[1]+diffx
    location2y = antena2[2]+diffy
       
    location1 = [location1x, location1y]
    location2 = [location2x, location2y]

    return location1, location2
############################################################
def calculate_antinode2(antena1, antena2, lenx, leny):

    diffx = antena2[1] - antena1[1]
    diffy = antena2[2] - antena1[2]
    l = []
    for i in range(lenx if lenx>leny else leny):
        location1x = antena1[1] - (diffx * i)
        location1y = antena1[2] - (diffy * i)
        location2x = antena2[1] + (diffx * i)
        location2y = antena2[2] + (diffy * i)
        if location1x >= 0 and location1x<lenx and location1y>=0 and location1y<leny:
            l.append([location1x, location1y])
        if location2x >= 0 and location2x<lenx and location2y>=0 and location2y<leny:
            l.append([location2x, location2y])
    return l
############################################################

main()