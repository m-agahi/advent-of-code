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
for line in input:
    temp=[]
    first_split= line.split(':')
    second_split=  first_split[1].split()
    for item in second_split:
        temp.append(int(item))
    p1.append(temp)

winnings=[]
for racenumber in range(len(p1[0])):
    race_time=p1[0][racenumber]
    race_record=p1[1][racenumber]
    wins=0
    for sec in range(race_time):
        speed = sec
        remaining_time=race_time-sec
        distance_travelled= remaining_time*speed
        if distance_travelled > race_record:
            wins +=1
    winnings.append(wins)

p1ans=1
for win in winnings:
    p1ans *= win
print(f"part 1: {p1ans}")


p2 = []
for line in input:
    temp=""
    first_split= line.split(':')
    second_split=  first_split[1].split()
    for item in second_split:
        temp += item
    p2.append(int(temp))

winnings=[]
race_time=p2[0]
race_record=p2[1]
wins=0
for sec in range(race_time):
    speed = sec
    remaining_time=race_time-sec
    distance_travelled= remaining_time*speed
    if distance_travelled > race_record:
        wins +=1
winnings.append(wins)

p2ans=1
for win in winnings:
    p2ans *= win
print(f"part 2: {p2ans}")