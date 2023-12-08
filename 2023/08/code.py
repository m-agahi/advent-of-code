import sys
from math import gcd

if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)
input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File not found or path is incorrect.")
###################################################################

values={
    'L': 0,
    'R': 1,
}

def compare(hand,check):
    result = 0
    for i in range(5):
        if hand[i]> check[i]:
            result = 1
            break
        elif hand[i] < check[i]:
            break
    return result

def part1():

    loc= "AAA"
    locinex = locations.index(loc)
    steps= 0
    while loc !="ZZZ":
        for instruction in p1_inst:
            steps +=1
            loc = p1_data[locinex][1][instruction]
            if loc == "ZZZ":
                break
            locinex = locations.index(loc)

    return steps
############################################################
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0
def lcm_numbers(numbers):
    lcm_val = 1
    for num in numbers:
        lcm_val = lcm(lcm_val, num)
    return lcm_val

def p2move(node,instruction):
    z = False
    next_node = node[1][instruction]
    node_index = locations.index(next_node)
    if next_node[-1] == "Z":     
        z = True
    return node_index,z

def part2():
    p2_starts = []
    for item in p1_data:
        if item[0][-1] == "A":
            loc = item[0]
            locindex = locations.index(loc)
            p2_starts.append(locindex)
    endz = []
    for i in range(len(p2_starts)):
        steps = 0
        z = False
        node = p1_data[p2_starts[i]]
        while z == False : 
            for instruction in p1_inst:
                steps += 1
                node_index,z = p2move(node,instruction)
                node= p1_data[node_index] 
                if z: break
        endz.append(steps)

    return lcm_numbers(endz)

    

############################################################
p1_inst= []
p1_data = []
p1_data_temp= input[2:]

for i in range (len(input[0])):
    p1_inst.append(values[input[0][i]])
for line in p1_data_temp:
        temp=[]
        first_split = line.split("=")
        second_split= first_split[1].split(",")
        s0= first_split[0][0:-1]
        s1= second_split[0][2:]
        temp.append(s0)
        s2=second_split[1][1:-1]
        temp.append([s1,s2])
        p1_data.append(temp)
locations = [sublist[0] for sublist in p1_data]


ans = part1()
print(f"part 1: {ans}")
ans =part2()
print(f"part 2: {ans}")





# def p2move(node_index,instruction):
#     z = False
#     node = p1_data[node_index][1][instruction]
#     node_index = locations.index(node)
#     if node[-1] == "Z":         
#         z = True
#     return node_index,z

# def part2():
#     p2_starts = []
#     for item in p1_data:
#         if item[0][-1] == "A":
#             loc = item[0]
#             locindex = locations.index(loc)
#             p2_starts.append(locindex)
#     steps = 0
#     endz = 0
#     while endz != len(p2_starts):
#         for instruction in p1_inst:
#             steps += 1
#             endz = 0
#             # print(instruction)
#             for startlist_index,  node_index in enumerate(p2_starts):
#                 ni ,z = p2move(node_index,instruction)
#                 p2_starts[startlist_index] = ni
#                 if z: endz += 1 
#             if endz == len(p2_starts): break
#         if endz > 1: print(f"{endz} - {steps}",end="\n")
#     print(f"part 2: {steps}")