from pathlib import Path
from pprint import pprint
from typing import List, Tuple

from pandas import DataFrame

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day8_input.txt") as file:
    data = file.read().splitlines()


def count_visible_trees(data: List[str]) -> int:
    trees = [list(row) for row in data]
    trees_df = DataFrame(trees)
    # print(trees_df)
    rows, cols = len(trees), len(trees[0])
    blank_df = trees_df.copy(deep=True)
    blank_df.iloc[0] = "x"
    blank_df.iloc[-1] = "x"
    blank_df[0].values[:] = "x"
    blank_df[cols - 1].values[:] = "x"

    perimeter = 2 * (len(trees) + len(trees[0])) - 4
    total = perimeter

    left = _look_from((rows, cols), trees_df, blank_df, "left")
    reversed_trees_df = _reverse_df(trees_df)
    reversed_blank_df = _reverse_df(blank_df)
    right = _look_from((rows, cols), reversed_trees_df, reversed_blank_df, "right")

    trees_df = _reverse_df(reversed_trees_df)
    blank_df = _reverse_df(reversed_blank_df)

    trees_df = trees_df.transpose()
    blank_df = blank_df.transpose()
    top = _look_from((rows, cols), trees_df, blank_df, "top")
    reversed_trees_df = _reverse_df(trees_df)
    reversed_blank_df = _reverse_df(blank_df)
    bottom = _look_from((rows, cols), reversed_trees_df, reversed_blank_df, "bottom")

    print(left, top, bottom, right)

    return total + left + top + bottom + right


def _reverse_df(df: DataFrame):
    reversed_df = df.copy(deep=True)
    reversed_df.columns = reversed(df.columns)
    reversed_df = reversed_df.iloc[:, ::-1]
    return reversed_df


def _look_from(
    end: Tuple[int], trees: DataFrame, blank: DataFrame, direction: str
) -> int:
    rs, cs = (0, 0)
    re, ce = end
    ri, ci = (1, 1)
    total = 0
    print(direction)
    for row_idx in range(rs, re, ri):
        prev = trees.iloc[row_idx][cs]
        for col_idx in range(cs, ce, ci):
            curr = trees.iloc[row_idx][col_idx]
            # if direction in ["right", "left"]:
            #     print(prev, curr)
            if blank.iloc[row_idx][col_idx] == "x":
                if curr > prev:
                    prev = curr
                continue
            if curr > prev:
                print(curr, prev)
                prev = curr
                total += 1
                blank.iloc[row_idx][col_idx] = "x"
    print(trees)
    print(blank)
    return total


print(count_visible_trees(data))
