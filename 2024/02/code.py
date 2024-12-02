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
    
    ans1,correct_list = part1(dataset)
    print(f"part 1: {ans1}")

    ans2 = part2(dataset,correct_list)
    print(f"part 2: {ans2+ans1}")

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        temp = [int(num) for num in line.split()]
        result.append(temp)
    # print(result) # Debugging
    return result

############################################################
def part1(dataset):
    correct_list = []
    correct_reports = 0
    for i in range(len(dataset)):
        if not is_sorted(dataset[i]):
            continue
        check_diff = True
        for j in range(len(dataset[i])-1):
            difference = abs(dataset[i][j] - dataset[i][j+1])
            if difference >3 or difference < 1:
                check_diff = False
                break
        if check_diff:
            correct_reports += 1
            correct_list.append(i)
            # print(dataset[i]) # Debugging
    return correct_reports, correct_list

############################################################
def is_sorted(data):
    is_sorted = (data == sorted(data)) or (data == sorted(data, reverse=True))
    return is_sorted

############################################################
def is_partially_sorted(lst):
    ascending_issues = 0
    descending_issues = 0
    direction = 0
    is_sorted= True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:  # Ascending order issue
            descending_issues += 1
        if lst[i] < lst[i + 1]:  # Descending order issue
            ascending_issues += 1
        if ascending_issues > 1 and descending_issues > 1:
            is_sorted= False
            break
    
    if ascending_issues > 1:
        direction = 1
    elif descending_issues > 1:
        direction = -1

    return (is_sorted, direction )

############################################################
def tolerate(data):
    check = False
    partially_sorted,direction = is_partially_sorted(data)
    popindex = -1
    if partially_sorted:
        number_of_pops = 0
        for i in range(0,len(data)-2):
            if data[i] == data[i+1]:
                number_of_pops += 1
                popindex = i
            elif direction == 1:
                if data[i] > data[i+1] :
                    number_of_pops += 1
                    popindex = i
                    # popindex = i+1
                elif data[i]+3 < data[i+1] :
                    number_of_pops += 1
                    popindex = i
                if i == len(data)-1:
                    if data[i] < data[i-1]:
                        number_of_pops += 1
                        popindex = i
            elif direction == -1:
                if data[i] < data[i+1] :
                    number_of_pops += 1
                    # popindex = i+1
                    popindex = i
                elif data[i] > data[i+1]+3 :
                    number_of_pops += 1
                    popindex = i
        if direction == 1:
            if data[-1] < data[-2]:
                number_of_pops += 1
                popindex = len(data)-1
        elif direction == -1:
            if data[-1] > data[-2]:
                number_of_pops += 1
                popindex = len(data)-1
        if data[-1] == data[-2]:
            number_of_pops += 1
            popindex = len(data)-1
        if number_of_pops < 2 and popindex != -1:
            data.pop(popindex)
        elif number_of_pops > 1:
            return False

        check_diff = True
        for j in range(len(data)-1):
            difference = abs(data[j] - data[j+1])
            if difference >3 or difference < 1:
                check_diff = False
                break
        check = check_diff
        if check:
            # print("data",data) # Debugging
            pass
        else:
            print("data",data)
    
    return check
############################################################
# FIXME: part 2 not working. need to reaproach the problem
def part2(dataset,correct_list):
    correct_reports = 0
    for i in range(len(dataset)):
        if i in correct_list:
            continue
        if tolerate(dataset[i]):
            correct_reports += 1
    return correct_reports
############################################################
main()