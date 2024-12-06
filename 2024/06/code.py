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
    dataset_original = readinput()
    dataset_original = convert_input(dataset_original)
    
    ans,path_taken = part1(copy.deepcopy(dataset_original))
    print(f"part 1: {ans}")
    
    ans = part2(copy.deepcopy(dataset_original), path_taken)
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    temp_row = []
    new_dataset = []
    
    for line in dataset:
        temp_row = [char for char in line]
        new_dataset.append(temp_row)

    return new_dataset

############################################################
def part1(dataset_p1):
    dataset = dataset_p1
    summary = 0
    found_init_location = False
    init_location= [0,0]
    row_numbers = len(dataset)
    column_numbers = len(dataset[0])
    
    for i in range(row_numbers):
        for j in range(column_numbers):
            if dataset[i][j] == "^":
                init_location = [i,j]
                found_init_location = True
                break
        if found_init_location:
            break
    
    print(init_location)
    current_position = init_location
    direction =[-1,0] # up
    path_taken = []
    while True:
        
        next_position = [current_position[0]+direction[0], current_position[1]+direction[1]]
        if next_position[0] < 0 or next_position[0] >= row_numbers or next_position[1] < 0 or next_position[1] >= column_numbers:
            dataset[current_position[0]][current_position[1]] = "X"
            path_taken.append(current_position)
            break
        if dataset[next_position[0]][next_position[1]] == "#":
            direction = turn_right(direction)
        else:
            dataset[current_position[0]][current_position[1]] = "X"
            path_taken.append(current_position)
            current_position = next_position

    summary = calculate_the_route(dataset)
    return summary, path_taken

############################################################
def part2(dataset_p2, path_taken):
    summary = 0
    loop_location = []
    current_position = path_taken[0]
    row_numbers = len(dataset_p2)
    column_numbers = len(dataset_p2[0])
    for i in range(len(path_taken)-1):
        dataset = copy.deepcopy(dataset_p2)
        if path_taken[i+1] != path_taken[0]:
            dataset[path_taken[i+1][0]][path_taken[i+1][1]] = "O"
        else:
            continue
        counter = 0
        loop = True
        direction =[-1,0] # up
        while counter<row_numbers*column_numbers:
            next_position = [current_position[0]+direction[0], current_position[1]+direction[1]]
            if next_position[0] < 0 or next_position[0] >= row_numbers or next_position[1] < 0 or next_position[1] >= column_numbers:
                dataset[current_position[0]][current_position[1]] = "X"
                loop = False
                break
            if dataset[next_position[0]][next_position[1]] == "#" or dataset[next_position[0]][next_position[1]] == "O":
                direction = turn_right(direction)
            else:
                dataset[current_position[0]][current_position[1]] = "X"
                current_position = next_position
                # fucking_visualize(dataset, current_position)
                counter += 1
        
        current_position = path_taken[0]
        if loop: 
            loop_location.append(path_taken[i+1])
            
    summary = len(set(tuple(item) for item in loop_location))

    return summary
############################################################
def calculate_the_route(dataset):
    summary = 0
    for row in dataset:
        for char in row:
            if char == "X":
                summary += 1    
    return summary

############################################################
def turn_right(direction):
    if direction == [-1,0]: # up
        return [0,1] # right
    if direction == [0,1]: # right
        return [1,0] # down
    if direction == [1,0]: # down
        return [0,-1] # left
    if direction == [0,-1]: # left
        return [-1,0] # up
############################################################
def fucking_visualize(dataset, index):
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')  # Works on Windows (cls) and Linux/Mac (clear)
    
    for i in range(len(dataset)):
        for j in range(len(dataset[0])):
            if i == index[0] and j == index[1]:
                print("O", end=" ")  # Highlight the target position
            else:
                print(dataset[i][j], end=" ")
        print()  # Newline for rows
    
    sleep(.08)


main()