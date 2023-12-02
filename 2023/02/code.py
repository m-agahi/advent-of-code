import sys

game_number_summary=0
color_power_summary=0
conditions = {
    'red': 12,
    'green': 13,
    'blue': 14
}

if len(sys.argv) != 2:
    print("Usage: python script_name.py input_filename")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        input = [line.strip() for line in file.readlines()]

except FileNotFoundError:
    print("File not found or path is incorrect.")


for line in input:
    valid = True
    color_max={
        'red':0,
        'green':0,
        'blue':0
    }
    line_parts = line.split(':')
    game_number = int(line_parts[0].split()[1])
    info_section = line_parts[1]
    info_section_split = info_section.split(';')
    for show in info_section_split :
        try:
            cubes = show.split(',')
        except:
            cubes = show
        for cube in cubes :
            number = int(cube.split()[0])
            color = cube.split()[1]
            if color_max.get(color) < number :
                color_max[color] = number
            if conditions.get(color) < number :
               valid= False
    if valid :
        game_number_summary +=game_number
    color_power =1
    for n in color_max.values():
        color_power *= n
    color_power_summary += color_power

print(game_number_summary)
print(color_power_summary)
