"""

--- Day 2: Red-Nosed Reports ---

   Fortunately, the first location The Historians want to search isn't a
   long walk from the Chief Historian's office.

   While the [15]Red-Nosed Reindeer nuclear fusion/fission plant appears
   to contain no sign of the Chief Historian, the engineers there run up
   to you as soon as they see you. Apparently, they still talk about the
   time Rudolph was saved through molecular synthesis from a single
   electron.

   They're quick to add that - since you're already here - they'd really
   appreciate your help analyzing some unusual data from the Red-Nosed
   reactor. You turn to check if The Historians are waiting for you, but
   they seem to have already divided into groups that are currently
   searching every corner of the facility. You offer to help with the
   unusual data.

   The unusual data (your puzzle input) consists of many reports, one
   report per line. Each report is a list of numbers called levels that
   are separated by spaces. For example:
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

   This example data contains six reports each containing five levels.

   The engineers are trying to figure out which reports are safe. The
   Red-Nosed reactor safety systems can only tolerate levels that are
   either gradually increasing or gradually decreasing. So, a report only
   counts as safe if both of the following are true:
     * The levels are either all increasing or all decreasing.
     * Any two adjacent levels differ by at least one and at most three.

   In the example above, the reports can be found safe or unsafe by
   checking those rules:
     * 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
     * 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
     * 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
     * 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
     * 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
     * 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or
       3.

   So, in this example, 2 reports are safe.

   Analyze the unusual data from the engineers. How many reports are safe?

   Your puzzle answer was 490.

   The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

   The engineers are surprised by the low number of safe reports until
   they realize they forgot to tell you about the Problem Dampener.

   The Problem Dampener is a reactor-mounted module that lets the reactor
   safety systems tolerate a single bad level in what would otherwise be a
   safe report. It's like the bad level never happened!

   Now, the same rules apply as before, except if removing a single level
   from an unsafe report would make it safe, the report instead counts as
   safe.

   More of the above example's reports are now safe:
     * 7 6 4 2 1: Safe without removing any level.
     * 1 2 7 8 9: Unsafe regardless of which level is removed.
     * 9 7 6 2 1: Unsafe regardless of which level is removed.
     * 1 3 2 4 5: Safe by removing the second level, 3.
     * 8 6 4 4 1: Safe by removing the third level, 4.
     * 1 3 6 7 9: Safe without removing any level.

   Thanks to the Problem Dampener, 4 reports are actually safe!

   Update your analysis by handling situations where the Problem Dampener
   can remove a single level from unsafe reports. How many reports are now
   safe?

   
"""

from pathlib import Path
from tkinter import W


def main() -> None:
    dir_path = Path(__file__).resolve().parent
    with open(f"{dir_path}/{Path(__file__).stem}_input.txt") as file:
        data = file.read().splitlines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


def part1(data: list[str]) -> int:
    def is_report_safe(report: list[int]) -> bool:
        levels = [int(level) for level in report]
        
        increasing = levels[0] < levels[1]
        
        for i in range(1, len(levels)):
            if (
                0 < abs(diff := (levels[i] - levels[i - 1])) <= 3
                and (diff > 0) == increasing
            ):
                continue
            return False
        return True

    reports = [line.split() for line in data]
    val = [is_report_safe([int(i) for i in report]) for report in reports]
    return sum(val)


def part2(data: list[str]) -> int:
    def is_report_safe(report: list[int]) -> bool:
        levels = [int(level) for level in report]
        queue: list[list[int]] = [levels]
        requeue = False
        # print(levels)
        
        while queue:
            curr = queue.pop()
            
            def process_row(row: list[int]) -> int:
                increasing = row[0] < row[1]
                # print(f'processing:{row}')
                for i in range(0, len(row)-1):
                    if (
                        0 < abs(diff := (row[i] - row[i + 1])) <= 3
                        and (diff < 0) == increasing
                    ):
                        continue
                    return i
                return -1
            first = process_row(curr)
            if first == -1:
                return True
            elif not requeue:
                requeue = True
                # print(f"{curr} failed at index {first}")
                second_curr = curr.copy()
                second_curr.pop(first)
                second = process_row(second_curr)
                third_curr = curr.copy()
                third_curr.pop(first-1)
                third = process_row(third_curr)
                fourth_curr = curr.copy()
                fourth_curr.pop(first+1)
                fourth = process_row(fourth_curr)
                return second == -1 or third == -1 or fourth == -1
        return False

    reports = [line.split() for line in data]
    val = [is_report_safe([int(i) for i in report]) for report in reports]
    # print(val)
    return sum(val)


if __name__ == "__main__":
    main()
