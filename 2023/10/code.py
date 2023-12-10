import sys
from math import gcd
from time import sleep
import math

############################################################
if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)
input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File not found or path is incorrect.")

############################################################
DirectionSet = {
    "n": "^",   
    "s": "v",
    "e": ">",
    "w": "<"
}
AllowedDirections = {
    "|" : ["n","s"], 
    "-" : ["e","w"], 
    "L" : ["n","e"],
    "J" : ["n","w"],
    "7" : ["w","s"],
    "F" : ["e","s"],
    "S" : ["n","e","s","w"],
    "." : []
}
DirectionCoordination = {
    "n": [-1,0],
    "s": [1,0],
    "e": [0,1],
    "w": [0,-1],
}

############################################################
def convert_input(dataset):
    result= []
    for line in dataset:
        temp=[]
        for i in range(len(line)):
            temp.append(line[i])
        result.append(temp)
    return result
############################################################
def findstart(dataset):
    sx,sy = 0,0
    for i in range(len(dataset)):
        for j in range(len(dataset)):
            if dataset[i][j] == "S":
                sx = i
                sy = j
    return [sx,sy]

############################################################
# def check_pipe(pipe,x,y,item,i,j):
#     direction = ""
#     if i==0:
#         if j== -1:
#             direction=pipeset["n"]
#         else:
#             direction=pipeset["s"]
#     elif j == 0:
#         if i == -1:
#             direction=pipeset["w"]
#         else:
#             direction=pipeset["e"]
#     return 

############################################################
# def StartPipe(x,y):
#     PipeAllowedDirections = AllowedDirections[pipe]
#     for direction in PipeAllowedDirections:
#         nx = x + DirectionCoordination[direction][0]
#         ny = y + DirectionCoordination[direction][1]
#         neighbor = dataset[nx][ny]

############################################################
def dirfrom(fr):
    temp = ""
    if fr == "n": 
        temp = "s"
    elif fr == "s":
        temp = "n"
    elif fr == "e":
        temp = "w"
    elif fr == "w":
        temp = "e"
    return temp

############################################################

def move(row,col,fr,step):
    pipe = dataset[row][col]
    directions = AllowedDirections[pipe]
    for direction in directions:
        if direction == fr: continue
        nr = row + DirectionCoordination[direction][0]
        nc = col + DirectionCoordination[direction][1]
        if nr > len(dataset)-1 or nc >len(dataset[0])-1:
            continue
        neighbor = dataset[nr][nc]
        # print(directions,fr, direction,neighbor)
        if neighbor == ".":
            # print("continue")
            continue
        else:
            # if dataset[row][col] != "S" : dataset[row][col] = DirectionSet[direction]
            char = "─"
            if (fr == "w" and directions == "e") or (fr == "e" and direction == "w") :
                char = "─"
            elif (fr == "w" and direction =="s") or (fr == "s" and direction =="w"):
                char = "┐"
            elif (fr == "e" and direction =="s") or (fr == "s" and direction =="e"):
                char = "┌"
            elif (fr == "n" and direction =="e") or (fr == "e" and direction =="n"):
                char = "└"
            elif (fr == "n" and direction =="w") or (fr == "w" and direction =="n"):
                char = "┘"
            elif (fr == "n" and direction =="s") or (fr == "s" and direction =="n"):
                char = "│"
            if dataset[row][col] != "S" : dataset[row][col] = char
            fr = direction
            row = nr
            col = nc
            break
    # for line in dataset: print(line)
        # print("")
    return row, col,fr

############################################################

def followloop(sx,sy,maxpossible):
    item = dataset[sx][sy]


    ## test 1
    # row = 1
    # col = 2
    # fr = "e"
    
    ## test 2
    # row = 2
    # col = 1
    # fr = "e"

    ## test 3
    # row = 1
    # col = 2
    # fr = "e"
     
    ## test 4
    # row = 1
    # col = 2
    # fr = "e"

    ## test 5
    # row = 4
    # col = 13
    # fr = "e"

    ## input
    row = 72
    col = 118
    fr = "w"

    steps = 0
    for i in range(maxpossible):
        fr = dirfrom(fr)
        row,col,fr = move(row,col,fr,steps)

        steps +=1
        if dataset[row][col] == "S": break
        # print(dataset[row][col])
        # print("next")
        # find sorrounding pipes
        # determine which ones are belong to the loop
        # choose the first one
        #follow loop
        # return the half of the loop length
    
    return steps

############################################################
def part1():
    maxpossible= (len(dataset))**2
    sxy = findstart(dataset)
    steps = followloop(sxy[0],sxy[1],maxpossible)

    return steps


############################################################
def part2():
    summary = 0
    for line in dataset:
        for i in range(len(line)):
            leftcount = 0
            rightcount = 0
            item = line[i]
            if item == ">" or item=="<" or item== "v" or item == "^" or item == "S": continue
            for j in range(0,i):
                check = line[j]
                if check== "v" or check == "^": leftcount +=1
            for j in range(i+1, len(line)):
                check = line[j]
                if check== "v" or check == "^": rightcount +=1
            if leftcount == 0 or rightcount == 0: 
                continue
            elif leftcount %2 == 0 and rightcount % 2 == 0:
                continue
            elif leftcount != rightcount:
                print(i,line[i])
                summary +=1
        print("")
    return summary




    
#     return summary

############################################################
############################################################

dataset = convert_input(input)
# print("start")
# ans = part1()/2
ans = math.ceil(part1()/2)
for line in dataset: 
    # print(line)
    for char in line:
        print(char,end='')
    print("")
print(f"part 1: {ans}")
ans = part2()
print(f"part 2: {ans}")
