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


number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

pattern = r'(?:one|two|three|four|five|six|seven|eight|nine)'
pattern_digit= r'\d'
dsum = 0
count = 0
for line in input:
    count += 1
    ds = 0
    de = 0
    matches = re.findall(pattern,line )
    text = line
    for match in matches:
        numeric_value = ''.join(number_mapping[word] for word in re.findall(r'\w+', match))
        text = text.replace(match, numeric_value, 1)
    digits_list = re.findall(pattern_digit, text)
    ds = int(digits_list[0])
    de = int(digits_list[-1])
    dsum+=(ds*10+de)
    print(f"{count} - {(ds*10)+de} {digits_list} {line}")
    
print(dsum)
    



