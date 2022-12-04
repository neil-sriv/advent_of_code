from typing import List, Tuple
import heapq


with open("day1_input.txt") as file:
    cases = [line.split('\n') for line in file.read().split('\n\n')]

def fat_elf(elves: List[List[str]]) -> int:
    largest_sum = 0
    for elf in elves:
        largest_sum = max(largest_sum, sum([int(cal) for cal in elf]))
    return largest_sum

def fat_elf_three(elvs: List[List[str]]) -> int:
    largest_sums = [0,0,0]
    for elf in elvs:
        _update_max(largest_sums, sum([int(cal) for cal in elf]))
    return sum(largest_sums)

def _update_max(largest_sums: List[int], current_sum: int):
    heapq.heappushpop(largest_sums, current_sum)

print(fat_elf_three(cases))