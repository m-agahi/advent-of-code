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
    ruleset,updateset = convert_input(dataset)
    
    ans,incorrect_orders = part1(ruleset,updateset)
    print(f"part 1: {ans}")

    ans = part2(ruleset,incorrect_orders)
    print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    ruleset = []
    updateset = []
    temp_updateset = []

    try:
        index = dataset.index('')
    except ValueError:
        print("Empty string not found in the list")
    ruleset = dataset[:index]
    temp_updateset = dataset[index+1:]
    for line in temp_updateset:
        temp=[int(item) for item in line.split(",")]
        updateset.append(temp)

    return ruleset, updateset

############################################################
def part1(ruleset, updateset):
    summary = 0
    incorrect_orders = []
    for update in updateset:
        if check_ruleset(update, ruleset):
            summary += find_middle_page(update)
        else:
            incorrect_orders.append(update)
    return summary, incorrect_orders

############################################################
def part2(ruleset, incorrect_orders):
    summary = 0
    for incorrect_order in incorrect_orders:
        fixed_order = fix_order(incorrect_order, ruleset)
        summary += find_middle_page(fixed_order)
    
    return summary
############################################################
def check_ruleset(update, ruleset):
    for page in update:
        correct_order = True
        for rule in ruleset:
            x = int(rule.split("|")[0])
            y = int(rule.split("|")[1])
            if page == x:
                for check in update[:update.index(page)]:
                    if check == y:
                        correct_order = False
                        break
            if not correct_order:
                break
        if not correct_order:
            break
    return correct_order
############################################################
def find_middle_page(update):
    middle_page = update[int((len(update)-1)/2)]
    return middle_page
############################################################
def fix_order(incorrect_order, ruleset):
    flag = True
    while flag:
        flag = False
        for i in range(len(incorrect_order)):
            for rule in ruleset:
                x = int(rule.split("|")[0])
                y = int(rule.split("|")[1])
                if incorrect_order[i] == x:
                    for j in range(i):
                        if incorrect_order[j] == y:
                            s1 = incorrect_order[i]
                            s2 = incorrect_order[j]
                            incorrect_order[i] = s2
                            incorrect_order[j] = s1
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
    return incorrect_order
############################################################
main()