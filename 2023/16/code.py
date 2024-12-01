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
    conditions,damaged = convert_input(dataset)
    # for line in conditions: print(line)
    # for line in damaged: print(line)

    ans = part1(conditions,damaged)
    print(f"part 1: {ans}")

    # ans = part2(dataset)
    # print(f"part 2: {ans}")

############################################################
def convert_input(dataset):
    conditions= []
    damaged = []

    for line in dataset:
        temp1=[]
        temp2=[]
        temp = line.split()
        # for i in range(len(temp[0])):
        #    temp1.append(temp[0][i])
        t = temp[0].split(".")
        for i in t:
            if len(i)>0:
                temp1.append(i)

        t = temp[1].split(",")
        for i in t:
            temp2.append(int(i))
        conditions.append(temp1)
        damaged.append(temp2)

    return conditions, damaged

############################################################
def calculate(conditions,condition,damaged,group,sumcheck,sumgoal,pos):

    blocklength = len(conditions[condition])
    binary_list = generate_binary_lists(blocklength)
    print(conditions[condition],pos)
    found = False
    if sumcheck == sumgoal:
        found = True
        pos +=1
        return pos , found
    for i in binary_list:
        for j in conditions[group]:
            if j == '#' and i == 1: 
                sumbin=0
                for digit in i:
                    sumbin += digit
                if sumbin == damaged[group]:
                    pos, found = calculate(conditions,condition+1,damaged,group+1,(sumbin+sumcheck),sumgoal,pos)
                    if found: break

# def calculate(conditions,conditionindex, damaged, group, sumcheck, sumgoal, pos):
#     blocklength = len(conditions[conditionindex])
#     print(conditions,pos)
#     found = False
#     if sumcheck == sumgoal:
#         found = True
#         pos += 1
#         return pos, found
    
#     for i in range(2 ** blocklength):
#         binary_list = [int(x) for x in list(bin(i)[2:].zfill(blocklength))]
#         sumbin = sum(binary_list)  # Sum of binary digits
        
#         if sumbin == damaged[group]:
#             # Now check if the condition matches '#' in binary list
#             match = True
#             for idx, j in enumerate(conditions[group]):
#                 if j == '#' and binary_list[idx] != 1:
#                     match = False
#                     break
            
#             if match:
#                 pos, found = calculate(
#                     conditions,conditionindex+1, damaged, group + 1, sumbin + sumcheck, sumgoal, pos
#                 )
#                 if found:
#                     break

#     return pos, found





     
############################################################

def generate_binary_lists(n):
    binary_list = []
    for i in range(2**n):
        binary_list.append([int(x) for x in list(bin(i)[2:].zfill(n))])
    return binary_list


############################################################
def part1(conditions,damaged):
    summary = 0
    for line in range(len(conditions)):
        sumgoal = 0
        pos = 0
        for group in range(len(damaged[line])):
            sumgoal += damaged[line][group]
        pos,_ = calculate(conditions[line],0,damaged[line],0,0,sumgoal,pos)
        summary += pos
    return summary

############################################################
def part2(dataset):
    pass    
############################################################
main()