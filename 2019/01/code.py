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


def result (number):
    number /=3
    number= math.floor(number)
    if number > 1:
        number -= 2
    elif number == 1:
        number = 0
    return number

sum1 = 0
sum2 = 0

for number in input:
    calculated = result(int(number))
    sum1 += calculated
    while calculated > 0:
        calculated = result(calculated) 
        sum2 += calculated
print (sum1,sum1+sum2)


