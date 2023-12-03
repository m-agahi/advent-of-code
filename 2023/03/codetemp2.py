from collections import defaultdict
from math import prod
from typing import Tuple, List, Dict


def parse_input(filename: str) -> list:
    with open(filename, "r") as input_file:
        return input_file.read().split("\n")


def complete_number(data: list, row: int, col: int) -> Tuple[str, set]:
    num, coordinates = "", set()
    while col < len(data[0]) and data[row][col].isdigit():
        num += data[row][col]
        coordinates.add((row, col))
        col += 1
    return num, coordinates


def find_numbers(data: list) -> List[Tuple[int, Dict[Tuple[int, int], str]]]:
    visited = set()
    numbers = []
    for i, row in enumerate(data):
        for j, ele in enumerate(row):
            if ele.isdigit() and (i, j) not in visited:
                number, coordinates = complete_number(data, i, j)
                visited |= coordinates
                neighbours = find_neighbours(data, coordinates)
                numbers.append((int(number), neighbours))
    return numbers


def find_neighbours(data: list, coordinates: set) -> Dict[Tuple[int, int], str]:
    neighbours = {}
    row_offset = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_offset = [-1, 0, 1, -1, 1, -1, 0, 1]
    for row, col in coordinates:
        for dr, dc in zip(row_offset, col_offset):
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) in coordinates:
                continue
            if (
                0 <= new_row < len(data)
                and 0 <= new_col < len(data[0])
                and data[new_row][new_col] != BLANK
            ):
                neighbours[new_row, new_col] = data[new_row][new_col]
    return neighbours


def part_two(numbers: list) -> int:
    gears = defaultdict(list)
    [
        gears[position].append(num)
        for num, neighbours in numbers
        for position, symbol in neighbours.items()
        if symbol == GEAR
    ]
    return sum(prod(nums) for nums in gears.values() if len(nums) == 2)


def main():
    data = parse_input(FILENAME)
    numbers = find_numbers(data)
    print(sum(num for num, neighbors in numbers if neighbors))
    print(part_two(numbers))


if __name__ == "__main__":
    BLANK = "."
    GEAR = "*"
    FILENAME = "input.txt"
    main()
