import sys
import math 
import math

############################################################
# if len(sys.argv) != 2:
#     print("Usage: python script_name.py input_filename")
#     sys.exit(1)
# input_file = sys.argv[1]
input_file = "./input.txt"
try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File not found or path is incorrect.")


def direction (character):
    direction = -1
    if character == "(":
        direction = 1     
    return direction

sum1 = 0
t = True
b =0

for index ,par in enumerate(input[0]):
    sum1+=direction(par)
    if sum1 < 0 and t:
        t = False
        b = index+1

print (sum1,b)


