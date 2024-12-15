import sys
import os
from math import gcd
from time import sleep
import math
import re
import copy
import termios

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
    warehouse_map,movements = convert_input(copy.deepcopy(input_dataset))
    
    # ans = part1(copy.deepcopy(dataset_original),100,11,7)
    ans = part1(copy.deepcopy(warehouse_map),movements)
    print(f"part 1: {ans}")
    
    # ans = part2(copy.deepcopy(dataset_original))
    # print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    wh_map = []
    movements = []
    for line in dataset[: dataset.index("")]:
        tmp = []
        for char in line:
            tmp.append(char)
        wh_map.append(tmp)

    for movement in dataset[dataset.index("")+1:]:
        movements.append(movement)
    mv_tmp = []
    for line in movements:
        for char in line:
            mv_tmp.append(char)
    movements = mv_tmp
    
    return wh_map,movements

############################################################
def part1(dataset_p1,movements):
    dataset = dataset_p1
    summary = 0
    robot_location = find_robot(dataset)
    print("Robot location: ",robot_location)
    for move in movements:
        robot_location = move_robot(dataset,robot_location,move)
    
    summary = calc_p1(dataset)
    return summary

############################################################
def part2(dataset_p2):
    dataset = dataset_p2
    summary = 0

    return summary

############################################################
def find_robot(dataset):
    for line in dataset:
        if "@" in line:
            location = (dataset.index(line),line.index("@"))
            break
    return location
############################################################
def move_robot(dataset,location,direction):
    # print(direction)
    direction = direction_to_move(direction)
    can_move,empty_index = check_move(dataset,location,direction)
    # print("direction: ",direction ,"Can move: ",can_move,"Empty index: ",empty_index)
    if can_move:
        dataset[location[0]][location[1]] = "."
        if direction[0] == 0:
            if direction[1] == 1:
                for i in range(empty_index[1],location[1],-1):
                    dataset[location[0]][i] = dataset[location[0]][i-1]
            else:
                for i in range(empty_index[1],location[1]):
                    dataset[location[0]][i] = dataset[location[0]][i+1]
        else:
            if direction[0] == 1:
                for i in range(empty_index[0],location[0],-1):
                    dataset[i][location[1]] = dataset[i-1][location[1]]
            else:
                for i in range(empty_index[0],location[0]):
                    dataset[i][location[1]] = dataset[i+1][location[1]]
        location = (location[0]+direction[0],location[1]+direction[1])
        dataset[location[0]][location[1]] = "@"
    # print (location)
    # for row in dataset:
    #     print("".join(row))
    # print("\n")
    # fucking_visualize(dataset)
    
    return location
############################################################
def direction_to_move(direction):
    if direction == "^":
        dir= [-1,0]
    elif direction == "v":
        dir= [1,0]
    elif direction == ">":
        dir= [0,1]
    elif direction == "<":
        dir= [0,-1]
    return dir
############################################################
def check_move(dataset,location,direction):
    can_move = False
    empty_index = []
    if direction[0] == 0:
        if direction[1] == 1:
            for i in range(location[1],len(dataset[0])):
                if dataset[location[0]][i] == "#":
                    break
                if dataset[location[0]][i] == ".":
                    can_move = True
                    empty_index=[location[0],i]
                    break
        else:
            for i in range(location[1],-1,-1):
                if dataset[location[0]][i] == "#":
                    break
                if dataset[location[0]][i] == ".":
                    can_move = True
                    empty_index=[location[0],i]
                    break
    else:
        if direction[0] == 1:
            for i in range(location[0],len(dataset)):
                if dataset[i][location[1]] == "#":
                    break
                if dataset[i][location[1]] == ".":
                    can_move = True
                    empty_index=[i,location[1]]
                    break
        else:
            for i in range(location[0],-1,-1):
                if dataset[i][location[1]] == "#":
                    break
                if dataset[i][location[1]] == ".":
                    can_move = True
                    empty_index=[i,location[1]]
                    break
    # print("empty index: ",empty_index)
    return can_move,empty_index
############################################################
def fucking_visualize(dataset):
    os.system('cls' if os.name == 'nt' else 'clear')  # Works on Windows (cls) and Linux/Mac (clear)
    for row in dataset:
        line = "".join(row)  
        
    wait_for_space()
        
############################################################
def wait_for_space():
    print("Press the space bar to continue...")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save current terminal settings
    try:
        # Set terminal to raw mode
        tty_settings = termios.tcgetattr(fd)
        tty_settings[3] = tty_settings[3] & ~termios.ICANON & ~termios.ECHO  # Disable canonical mode and echo
        termios.tcsetattr(fd, termios.TCSADRAIN, tty_settings)
        while True:
            char = sys.stdin.read(1)
            if char == " ":
                break
    finally:
        # Restore original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
############################################################
def calc_p1(dataset):
    for row in dataset:
        print("".join(row))
    summary = 0
    for i in range(len(dataset)):
        for j in range(len(dataset[0])):
            if dataset[i][j] == "O":
                # print("O found at: ",i,j," value: ",i*100+j)
                summary += i*100+j

    return summary
############################################################
main()