"""

--- Day 3: Gear Ratios ---

   You and the Elf eventually reach a [15]gondola lift station; he says
   the gondola lift will take you up to the water source, but this is as
   far as he can bring you. You go inside.

   It doesn't take long to find the gondolas, but there seems to be a
   problem: they're not moving.

   "Aaah!"

   You turn around to see a slightly-greasy Elf with a wrench and a look
   of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
   working right now; it'll still be a while before I can fix it." You
   offer to help.

   The engineer explains that an engine part seems to be missing from the
   engine, but nobody can figure out which one. If you can add up all the
   part numbers in the engine schematic, it should be easy to work out
   which part is missing.

   The engine schematic (your puzzle input) consists of a visual
   representation of the engine. There are lots of numbers and symbols you
   don't really understand, but apparently any number adjacent to a
   symbol, even diagonally, is a "part number" and should be included in
   your sum. (Periods (.) do not count as a symbol.)

   Here is an example engine schematic:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

   In this schematic, two numbers are not part numbers because they are
   not adjacent to a symbol: 114 (top right) and 58 (middle right). Every
   other number is adjacent to a symbol and so is a part number; their sum
   is 4361.

   Of course, the actual engine schematic is much larger. What is the sum
   of all of the part numbers in the engine schematic?

   Your puzzle answer was 550934.

   The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

   The engineer finds the missing part and installs it in the engine! As
   the engine springs to life, you jump in the closest gondola, finally
   ready to ascend to the water source.

   You don't seem to be going very fast, though. Maybe something is still
   wrong? Fortunately, the gondola has a phone labeled "help", so you pick
   it up and the engineer answers.

   Before you can explain the situation, she suggests that you look out
   the window. There stands the engineer, holding a phone in one hand and
   waving with the other. You're going so slowly that you haven't even
   left the station. You exit the gondola.

   The missing part wasn't the only issue - one of the gears in the engine
   is wrong. A gear is any * symbol that is adjacent to exactly two part
   numbers. Its gear ratio is the result of multiplying those two numbers
   together.

   This time, you need to find the gear ratio of every gear and add them
   all up so that the engineer can figure out which gear needs to be
   replaced.

   Consider the same engine schematic again:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

   In this schematic, there are two gears. The first is in the top left;
   it has part numbers 467 and 35, so its gear ratio is 16345. The second
   gear is in the lower right; its gear ratio is 451490. (The * adjacent
   to 617 is not a gear because it is only adjacent to one part number.)
   Adding up all of the gear ratios produces 467835.

   What is the sum of all of the gear ratios in your engine schematic?

   
"""

from pathlib import Path
from copy import deepcopy


def main() -> None:
    dir_path = Path(__file__).resolve().parent
    with open(f"{dir_path}/{Path(__file__).stem}_input.txt") as file:
        data = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


def part1(data: list[str]) -> int:
    grid = [list(line) for line in data]
    total = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                total += sum([num[0] for num in _adjacent(grid, i, j)])
    return total


def _adjacent(
    grid: list[list[str]], i: int, j: int, 
) -> list[tuple[int, int]]:
    grid_cp = deepcopy(grid)
    nums: list[tuple[int, int]] = []
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            if (col < 0 or col > len(grid_cp[row])) or (row < 0 or row > len(grid_cp)):
                continue
            if grid_cp[row][col].isnumeric():
                nums.append(_parse_number(grid_cp, row, col))
                _remove_number(grid_cp, row, nums[-1][-1])
    return nums


def _parse_number(grid: list[list[str]], i: int, j: int) -> tuple[int, int]:
    n = ""
    start = j
    while start >= 0 and grid[i][start].isnumeric():
        start -= 1
    start += 1
    end = start
    while end < len(grid[i]) and grid[i][end].isnumeric():
        end += 1
    end -= 1
    for idx in range(start, end + 1):
        n += grid[i][idx]
    return int(n), end


def _remove_number(grid: list[list[str]], i: int, j: int) -> None:
    while j >= 0 and grid[i][j].isnumeric():
        grid[i][j] = "."
        j -= 1


def part2(data: list[str]) -> int:
    grid = [list(line) for line in data]
    total = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                nums = _adjacent(grid, i, j)
                if len(nums)== 2:
                    total += nums[0][0] * nums[1][0]
    return total


if __name__ == "__main__":
    main()
