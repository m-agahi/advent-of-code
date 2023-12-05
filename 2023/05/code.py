import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)
input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File not found or path is incorrect.")

p1 = []
counter=0
seeds= input[0].split(':')[1].split()

templist=[]
for seed in seeds:
    pair=[-1,int(seed)]
    templist.append(pair)
p1.insert(0,templist)


line = 2
while line < len(input)-1:
    templist=[]
    first_split = input[line].split(':')
    second_split = first_split[0].split()
    linecount=0
    for mapping in range(line+1 ,len(input)):
        linecount +=1
        if len(input[mapping]) == 0: break
        fs = input[mapping].split()
        t=[int(fs[1]),int(fs[0]),int(fs[2])]
        templist.append(t)
    line += linecount+1
    counter +=1
    p1.append(templist)

last = []
for i in range(len(p1[0])):
    pair = p1[0][i]
    d1 = pair[1]
    for j in range(1,len(p1)):
        for k in range(len(p1[j])) :
            check = p1[j][k]
            s2 = check[0]
            d2 = check[1]
            counter= check[2]
            if (d1 >= s2  ) and (d1 <= s2 + counter):
                d1 = d2 + (d1 - s2)
                break
    # print(f"{i} : {d1}")
    last.append(d1)

minimun = 9999999999
for item in last:
    if item < minimun:
        minimun = item
print(f"part 1: {minimun}")

################# part 2
p2 = []
templist=[]
for i in range( 0 , len(seeds), 2) :
    # print(i)
    pair=[int(seeds[i]),int(seeds[i+1])]
    templist.append(pair)
p2.insert(0,templist)

line = 2
while line < len(input)-1:
    templist=[]
    first_split = input[line].split(':')
    second_split = first_split[0].split()
    linecount=0
    for mapping in range(line+1 ,len(input)):
        linecount +=1
        if len(input[mapping]) == 0: break
        fs = input[mapping].split()
        t=[int(fs[1]),int(fs[0]),int(fs[2])]
        templist.append(t)
    line += linecount+1
    counter +=1
    p2.append(templist)

last = []
for i in range(len(p2[0])):
    pair = p2[0][i]
    s1 = pair[0]
    c1 = pair[1]
    for fuck in range(s1,s1+c1):
        d1 = fuck
        for j in range(1,len(p2)):
            for k in range(len(p2[j])) :
                check = p2[j][k]
                s2 = check[0]
                d2 = check[1]
                counter= check[2]
                if (d1 >= s2) and (d1 <= s2 + counter):
                    d1 = d2 + (d1 - s2)
                    break
        last.append(d1)
    print(f".",end="")

minimun = 9999999999
for item in last:
    if item < minimun:
        minimun = item
print(f"part 2: {minimun}")