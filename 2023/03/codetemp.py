SYMBOLS = "!@#$%^&*()_+-=\][{}|:;/?<>"

with open("input.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

grid = []
ans = 0

for line in data:
    grid.append(list(line))

for i, row in enumerate(grid):
    index = 0
    while index < len(row):
        if row[index].isnumeric():
            positions = []
            num = row[index]
            positions.append(index)
            ended = False
            index += 1
            while not ended and index < len(row):
                if row[index].isnumeric():
                    num += row[index]
                    positions.append(index)
                    index += 1
                else:
                    ended = True

            num = int(num)
            adjacent_chars = []

            if positions[0] != 0:  # left
                adjacent_chars.append(grid[i][positions[0] - 1])
            if positions[0] != 0 and i != 0:  # top left
                adjacent_chars.append(grid[i - 1][positions[0] - 1])
            if positions[-1] + 1 != len(row) and i != 0:  # top right
                adjacent_chars.append(grid[i - 1][positions[-1] + 1])
            if positions[-1] + 1 != len(row):  # right
                adjacent_chars.append(grid[i][positions[-1] + 1])
            if positions[-1] + 1 != len(row) and i + 1 != len(grid):  # bottom right
                adjacent_chars.append(grid[i + 1][positions[-1] + 1])
            if positions[0] != 0 and i + 1 != len(grid):  # bottom left
                adjacent_chars.append(grid[i + 1][positions[0] - 1])

            if len(positions) == 1:
                if i != 0:  # top
                    adjacent_chars += [grid[i - 1][positions[0]]]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars += [grid[i + 1][positions[0]]]

            elif len(positions) == 2:
                if i != 0:  # top
                    adjacent_chars += [grid[i - 1]
                                       [positions[0]], grid[i - 1][positions[1]]]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars += [grid[i + 1][positions[0]],
                                       grid[i + 1][positions[1]]]

            elif len(positions) == 3:
                if i != 0:  # top
                    adjacent_chars += [grid[i - 1][positions[0]],
                                       grid[i - 1][positions[1]], grid[i - 1][positions[2]]]
                if i + 1 != len(grid):  # bottom
                    adjacent_chars += [grid[i + 1][positions[0]], grid[i + 1]
                                       [positions[1]], grid[i + 1][positions[2]]]

            if any(adjacent_char in SYMBOLS for adjacent_char in adjacent_chars):
                ans += num
                print(f"{i+1} {num}")

        index += 1

print(ans)