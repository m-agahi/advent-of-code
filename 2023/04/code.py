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

hit_sum = 0
for line in input:
    hit = 0
    first_split = line.split(':')
    second_split = first_split[1].split('|')
    winning_numbers = second_split[0].split() 
    check_numbers = second_split[1].split()
    for d1 in winning_numbers:
        for d2 in check_numbers:
            if d1 == d2: hit +=1
    if hit>0:  
        hit_sum += 2**(hit-1)

print(f"part 1: {hit_sum}")
print("part 2 calculations take a bit of time. wait...")

part2 = input
for line in part2:
    hit = 0
    first_split = line.split(':')
    second_split = first_split[1].split('|')
    winning_numbers = second_split[0].split() 
    check_numbers = second_split[1].split()
    card_number= int(first_split[0].split()[1])
    for d1 in winning_numbers:
        for d2 in check_numbers:
            if d1 == d2: hit +=1
    for count in range(hit):
        part2.append(input[card_number+count])

print(f"part 2: {len(part2)}")