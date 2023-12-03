import sys
import re

test_answer=4361

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
    # print(input[line])
    # print(line)
    for pair in fullnumlist[line]:
        # print(pair)
        valid=False
        pairlen=len(pair[0])
        # print(pair[1]+pairlen)
        try:
            if line>0:
                if pair[1]>0:
                    if input[line-1][pair[1]-1] != '.': valid = True
                if pair[1]+ pairlen < len(input[line]):
                    if input[line-1][pair[1]+pairlen] != '.': valid = True
                for digit in range(pairlen):
                    if input[line-1][pair[1]+digit] != '.': valid = True
            if line < len(fullnumlist)-1:
                if pair[1]>0:
                    if input[line+1][pair[1]-1] != '.': valid = True
                if pair[1]+ pairlen < len(input[line]):
                    if input[line+1][pair[1]+pairlen] != '.': valid = True
                for digit in range(pairlen):
                    if input[line+1][pair[1]+digit] != '.': valid = True
            if pair[1]>0:
                if input[line][pair[1]-1] != '.': valid = True
            if pair[1]+ pairlen < len(input[line]):
                if input[line][pair[1]+pairlen] != '.': valid = True        
        except:
            print(f"{line} {pair[1]} {len(input[line])}")
        if valid:
            print(pair)
            sum += int(pair[0])
            

print(sum)
