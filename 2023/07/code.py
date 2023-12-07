import sys
from collections import Counter

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
def categorize(hand):
    frequency = Counter(hand)
    jokers =0
    for card in hand:
        if card == 11:
            jokers +=1
    comms = frequency.most_common(5)
    r1 = comms[0][1]
    if len(comms)>1:
        r2= comms[1][1]
    else:
        r2=0

    if r1 == 5:
        if comms[0][0]==11: 
            jokers = 0
        cat = 7
    elif r1 == 4:
        if comms[0][0]==11: 
            jokers = 1
        cat = 6
    elif r1 == 3 :
        if r2 == 2: 
            if comms[0][0]==11:  
                jokers = 2
            cat = 5
        else: 
            if comms[0][0]==11: 
                jokers = 2
            if jokers == 1: 
                jokers = 2
            cat = 4
    elif r1 == 2: 
        if r2 == 2:
            if comms[0][0]==11 or comms[1][0]== 11 : 
                jokers = 3
            if len(comms) > 2: 
                if comms[2][0] == 11: 
                    jokers = 2
            cat = 3
        else:
            if jokers == 1: 
                jokers = 2
            cat = 2
    else:
        cat = 1
    return [cat,cat+jokers]

def compare(hand,check):
    result = 0
    for i in range(5):
        if hand[i]> check[i]:
            result = 1
            break
        elif hand[i] < check[i]:
            break
    return result

values={
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

###############################p1
p1 = []
for line in input:
    temp=[]
    first_split= line.split()
    for item in first_split[0]:
        temp.append(values[item])
    cat1 = categorize(temp)[0]
    cat2= categorize(temp)[1]
    temp.append(cat1)
    temp.append(cat2)
    temp.append(int(first_split[1]))
    p1.append(temp)

max_power= len(p1)


for item in range(max_power):
    power = 1
    for check in range(max_power):
        if item == check:
            continue
        if p1[item][5] > p1[check][5]:
            power +=1
        elif p1[item][5] == p1[check][5]:
            res = compare(p1[item],p1[check])
            power += res
    p1[item].append(power)
winnings = 0
for item in p1:
    winnings += item[7]*item[8]
print(f"part 1: {winnings}")

######################### p2
p2=[]

for item in p1:
    temp=[]
    for i in range(5):
        d = item[i]
        if d == 11:
            d=1
        temp.append(d)
    temp.append(item[6])
    temp.append(item[7])
    p2.append(temp)

for item in range(max_power):
    power = 1
    for check in range(max_power):
        if item == check:
            continue
        if p2[item][5] > p2[check][5]:
            power +=1
        elif p2[item][5] == p2[check][5]:
            res = compare(p2[item],p2[check])
            power += res
    p2[item].append(power)

winnings = 0
for item in p2:
    winnings += item[6]*item[7]
print(f"part 2: {winnings}")