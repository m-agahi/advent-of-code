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
    dataset_original = convert_input(copy.deepcopy(input_dataset))
    
    # ans = part1(copy.deepcopy(dataset_original),100,11,7)
    ans = part1(copy.deepcopy(dataset_original),100,101,103)
    print(f"part 1: {ans}")
    
    ans = part2(copy.deepcopy(dataset_original))
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    new_dataset = []
    for line in dataset:
        p = line.split(" ")[0]
        v = line.split(" ")[1]
        px = p.split(",")[0][2:]
        py = p.split(",")[1]
        vx = v.split(",")[0][2:]
        vy = v.split(",")[1]
        temp_row = [[int(px), int(py)], [int(vx), int(vy)]]
        new_dataset.append(temp_row)
    
    return new_dataset

############################################################
def part1(dataset_p1,seconds,lenx,leny):
    dataset = dataset_p1
    summary = 0
    new_locations = []
    for robot in dataset:
        fin_loc_raw = [robot[1][0]*seconds, robot[1][1]*seconds]
        new_locations.append([robot[0], fin_loc_raw])
    
    final_locations = []
    for robot in new_locations:
        # pxt = abs(robot[1][0]) % lenx 
        # pyt = abs(robot[1][1]) % leny
        pxt = abs(robot[1][0])
        pyt = abs(robot[1][1])
        xsign = 1 if robot[1][0] > 0 else -1
        ysign = 1 if robot[1][1] > 0 else -1

        if xsign == 1:
            px = (robot[0][0] + pxt) % lenx
        else:
            px = (robot[0][0] - pxt) % lenx
        
        if ysign == 1:
            py = (robot[0][1] + pyt) % leny
        else:
            py = (robot[0][1] + (leny - (pyt % leny))) % leny

        final_locations.append([robot[0],[px, py]])
    
    midx = lenx//2
    midy = leny//2
    sq1 = sq2 = sq3 = sq4 = 0
    for robot in final_locations:
        if robot[1][0] == midx or robot[1][1] == midy:
            continue
        else:
            if robot[1][0] < midx and robot[1][1] < midy:
                sq1 += 1
            elif robot[1][0] > midx and robot[1][1] < midy:
                sq2 += 1
            elif robot[1][0] > midx and robot[1][1] > midy:
                sq3 += 1
            elif robot[1][0] < midx and robot[1][1] > midy:
                sq4 += 1
    print(sq1,sq2,sq3,sq4)
    summary = sq1 * sq2 * sq3 * sq4

    return summary

############################################################
def part2(dataset_p2):
    lenx = 101
    leny = 103
    dataset = dataset_p2
    summary = 0
    for seconds in range (1,100000):
        new_locations = []
        for robot in dataset:
            fin_loc_raw = [robot[1][0]*seconds, robot[1][1]*seconds]
            new_locations.append([robot[0], fin_loc_raw])
        
        final_locations = []
        for robot in new_locations:
            # pxt = abs(robot[1][0]) % lenx 
            # pyt = abs(robot[1][1]) % leny
            pxt = abs(robot[1][0])
            pyt = abs(robot[1][1])
            xsign = 1 if robot[1][0] > 0 else -1
            ysign = 1 if robot[1][1] > 0 else -1

            if xsign == 1:
                px = (robot[0][0] + pxt) % lenx
            else:
                px = (robot[0][0] - pxt) % lenx
            
            if ysign == 1:
                py = (robot[0][1] + pyt) % leny
            else:
                py = (robot[0][1] + (leny - (pyt % leny))) % leny

            final_locations.append([robot[0],[px, py]])
        fucking_visualize(final_locations,seconds)

    return summary

############################################################
def fucking_visualize(dataset,seconds):
    os.system('cls' if os.name == 'nt' else 'clear')  # Works on Windows (cls) and Linux/Mac (clear)
    matrix = [[" " for i in range(105)] for j in range(105)]
    for robot in dataset:
        x = robot[1][0]
        y = robot[1][1]
        matrix[x][y] = "#"
    print(f"Seconds: {seconds}")
    flag = False
    pattern = "#" * 10
    for row in matrix:
        line = "".join(row)  
        if re.search(pattern, line):  
            flag = True
            break  
    if not flag:
        return
    for row in matrix:
        print("".join(row))
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
main()