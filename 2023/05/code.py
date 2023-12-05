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

processes_map = []
seedstosoil=[]

counter=0

seeds= input[0].split(':')[1].split()
templist=[]
for seed in seeds:
    pair=[seed,"-1"]
    templist.append(pair)
processes_map.insert(0,templist)
# print(processes_map)
# print(processes_map[0])

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
        templist.append(fs)
    line += linecount+1
    counter +=1
    processes_map.append(templist)

# for line in processes_map:
#     for index in line:
#         print(index)
#     print("")
# print(processes_map[0])
expanded=[]
expanded.insert(0,processes_map[0]) 
# print(expanded[0])

for tabel in range(1,len(processes_map)):
    templist= []
    for resourceindex in range (len(processes_map[tabel])):
        srcresourcestart=int(processes_map[tabel][resourceindex][1])
        dstresourcestart=int(processes_map[tabel][resourceindex][0])
        count = int(processes_map[tabel][resourceindex][2])
        for counter in range(count):
            pair = [srcresourcestart+counter ,dstresourcestart+counter ]
            templist.append(pair)
        # templist.insert(0,temppairlist)  
    # for line in expanded[tabel]:
    #     # print(line)
    #     pass
        #     # for pair in line:
        #     #     print(pair)
        #     # print("")
        # # print("")
    expanded.append(templist)  
final_map=[]
final_map.insert(0,expanded[0])


# i1=0
for i1 in range(len(expanded)-1):
    templist=[]
    for src in expanded[i1]:
        found = False
        for dst in expanded[i1+1]:
            if int(src[0]) == int(dst[0]) and not found :
                found=True
                templist.append(dst)
                # print("found")
                # break
        if not found :
            temp=[int(src[0]),int(src[0])]
            templist.append(temp)
            # print(i1)
            # print(temp)
            # temp = [src[0],src[0]]
            # break
    expanded[i1+1] = templist
    print(templist)
    print(expanded[i1+1])

    # final_map.append(templist)
    # i1 +=1
    # if i1 >= len(expanded)-1:
    #     break
    # print(i1)
                # pass
        #     print(tabel)
        #     print(expanded[tabel])
        # for check in expanded[tabel]:
        #     if pair[0] == check[0]:
        #         found = True
        # if not found:
        #     expanded.append([pair[0],pair[0]])

# print(final_map)

# minimum = final_map[7][0][1]
# print(minimum)
# for line in final_map:
#     print(line)
#     print("")
# for line in expanded:
#     print(expanded)
#     print("")
# print("#¤##########################")
# for line in range ( len(expanded) ):
#     print(f"{line} : {expanded[line]}")
#     print("")

# seed 1 :soil = 2
# if seed not in the list add seed to soil equal

# soil2 = fert 3
# if soil not in fert add soil2

