from typing import List


with open("day3_input.txt") as file:
    data = file.read().splitlines()


def find_item(rucksack: str) -> int:
    one, two = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    (item,) = set(one).intersection(set(two))
    return _calculate_priority(item)


def sum_items(rucksacks: List[str]) -> int:
    return sum([find_item(rucksack) for rucksack in rucksacks])


def find_badges(rucksacks: List[str]) -> int:
    total = 0
    for group in range(0, len(rucksacks), 3):
        total += find_badge(rucksacks[group : group + 3])
    return total


def _calculate_priority(letter: str) -> int:
    return ord(letter) - 64 + 26 if letter.isupper() else ord(letter) - 96


def find_badge(rucksacks: List[str]) -> int:
    (item,) = set.intersection(*[set(rucksack) for rucksack in rucksacks])
    return _calculate_priority(item)


print(sum_items(data))
print(find_badges(data))
