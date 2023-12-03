import sys
import re

if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]

except FileNotFoundError:
    print("File not found or path is incorrect.")

fullnumlist=[]
sum=0
for line in input:
    numbers = re.findall(r'\d+', line)
    numlist=[]
    for number in numbers:
        startindex= re.search(number, line).start()
        temp = [number,startindex]
        numlist.append(temp)
    fullnumlist.append(numlist)

for line in range(len(fullnumlist)):
    for pair in fullnumlist[line]:
        valid=False
        pairlen=len(pair[0])
        try:
            if line>0:
                if pair[1]>0:
                    if (not(input[line-1][pair[1]-1].isdigit()) and input[line-1][pair[1]-1] != '.'): valid = True 
                if pair[1]+ pairlen < len(input[line]):
                    if (not(input[line-1][pair[1]+pairlen].isdigit()) and input[line-1][pair[1]+pairlen] != '.'): valid = True 
                for digit in range(pairlen):
                    if (not(input[line-1][pair[1]+digit].isdigit()) and input[line-1][pair[1]+digit] != '.'): valid = True
            if line < len(fullnumlist)-1:
                if pair[1]>0:
                    if (not(input[line+1][pair[1]-1].isdigit()) and input[line+1][pair[1]-1] != '.'): valid = True
                if pair[1]+ pairlen < len(input[line]):
                    if (not(input[line+1][pair[1]+pairlen].isdigit()) and input[line+1][pair[1]+pairlen] != '.'): valid = True
                for digit in range(pairlen):
                    if (not(input[line+1][pair[1]+digit].isdigit()) and input[line+1][pair[1]+digit] != '.'): valid = True
            if pair[1]>0:
                if (not(input[line][pair[1]-1].isdigit()) and input[line][pair[1]-1] != '.'): valid = True
            if pair[1]+ pairlen < len(input[line]):
                if (not(input[line][pair[1]+pairlen].isdigit()) and input[line][pair[1]+pairlen] != '.'): valid = True        
        except:
            print(f"exception on line {line+1} : index {pair[1]}")
        if valid:
            print(f"{pair[0]}",end=' ')
            # print(f"{line+1} {pair[0]}")
            sum += int(pair[0])
    print("")
print(f"part1: {sum}")

# asterisk = []
# for line in range(len(input)):
#     data = input[line]
#     lendata = len(data)
#     starlist=[]
#     for index in range(lendata):
#         if data[index] == "*": 
#             temp=[line,index]
#             starlist.append(temp)
#     if len(starlist)>0 :
#         asterisk.append(starlist)
#             # print(f"{line} {index} is *")
# for line in asterisk:
#     print(line)

