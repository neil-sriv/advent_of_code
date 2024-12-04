"""

--- Day 4: Ceres Search ---

   "Looks like the Chief's not here. Next!" One of The Historians pulls
   out a device and pushes the only button on it. After a brief flash, you
   recognize the interior of the [15]Ceres monitoring station!

   As the search for the Chief continues, a small Elf who lives on the
   station tugs on your shirt; she'd like to know if you could help her
   with her word search (your puzzle input). She only has to find one
   word: XMAS.

   This word search allows words to be horizontal, vertical, diagonal,
   written backwards, or even overlapping other words. It's a little
   unusual, though, as you don't merely need to find one instance of XMAS
   - you need to find all of them. Here are a few ways XMAS might appear,
   where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

   The actual word search will be full of letters instead. For example:
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

   In this word search, XMAS occurs a total of 18 times; here's the same
   word search again, but where letters not involved in any XMAS have been
   replaced with .:
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

   Take a look at the little Elf's word search. How many times does XMAS
   appear?

   Your puzzle answer was 2447.

   The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

   The Elf looks quizzically at you. Did you misunderstand the assignment?

   Looking for the instructions, you flip over the word search to find
   that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which
   you're supposed to find two MAS in the shape of an X. One way to
   achieve that is like this:
M.S
.A.
M.S

   Irrelevant characters have again been replaced with . in the above
   diagram. Within the X, each MAS can be written forwards or backwards.

   Here's the same example from before, but this time all of the X-MASes
   have been kept instead:
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

   In this example, an X-MAS appears 9 times.

   Flip the word search from the instructions back over to the word search
   side and try again. How many times does an X-MAS appear?


"""

from pathlib import Path

import numpy as np
import regex as re


def main() -> None:
    dir_path = Path(__file__).resolve().parent
    with open(f"{dir_path}/{Path(__file__).stem}_input.txt") as file:
        data = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


def horizontal(data: str) -> int:
    total = 0
    regexp = r"(XMAS)|(SAMX)"
    result = re.findall(regexp, data, overlapped=True)
    total = sum([2 if left and right else 1 for left, right in result])
    return total


def diag(data: list[list[str]], coordinate: tuple[int, int]) -> int:
    y, x = coordinate
    # base case
    lists: list[list[str]] = []
    if 3 <= x:
        if 3 <= y:
            uleft = [data[y - n][x - n] for n in range(4)]
            lists.append(uleft)
        if y < len(data) - 3:
            dleft = [data[y + n][x - n] for n in range(4)]
            lists.append(dleft)
    if x < len(data[0]) - 3:
        if 3 <= y:
            uright = [data[y - n][x + n] for n in range(4)]
            lists.append(uright)
        if y < len(data) - 3:
            dright = [data[y + n][x + n] for n in range(4)]
            lists.append(dright)
    total = sum(
        [1 if "".join(diag) in ["XMAS", "SAMX"] else 0 for diag in lists]
    )
    return total


def diagM(data: list[list[str]], coordinate: tuple[int, int]) -> int:
    y, x = coordinate
    # base case
    if 1 <= x < len(data[0]) - 1 and 1 <= y < len(data) - 1:
        major = [data[y - 1][x - 1], "A", data[y + 1][x + 1]]
        minor = [data[y + 1][x - 1], "A", data[y - 1][x + 1]]
        total = sum(
            [
                1 if "".join(diag) in ["MAS", "SAM"] else 0
                for diag in [major, minor]
            ]
        )
        return total // 2 if total == 2 else 0
    return 0


def part1(data: list[str]) -> int:
    # find all X coordinates
    xs: list[tuple[int, int]] = []
    grid: list[list[str]] = []
    total = 0
    for i, row in enumerate(data):
        grid.append(list(row))
        total += horizontal(row)
        for j, c in enumerate(row):
            if c == "X":
                xs.append((i, j))
    transposed = list(zip(*grid))
    for col in transposed:
        total += horizontal("".join(col))
    for coordinate in xs:
        total += diag(grid, coordinate)
    return total


def part2(data: list[str]) -> int:
    # find all A coordinates
    xs: list[tuple[int, int]] = []
    grid: list[list[str]] = []
    total = 0
    for i, row in enumerate(data):
        grid.append(list(row))
        for j, c in enumerate(row):
            if c == "A":
                xs.append((i, j))
    for coordinate in xs:
        total += diagM(grid, coordinate)
    return total


if __name__ == "__main__":
    main()
