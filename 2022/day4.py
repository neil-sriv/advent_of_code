from itertools import permutations, chain
from typing import Any, List


with open("day4_input.txt") as file:
    data = [line.split(",") for line in file.read().splitlines()]


def find_contained_pairs(pairs: List[List[str]]) -> int:
    total = sum(
        [
            is_contained(*pairing)
            for pairing in set(
                chain.from_iterable([permutations(pair) for pair in pairs])
            )
        ]
    )
    return total


def find_contained_pairs_boring(pairs: List[List[str]]) -> int:
    total = sum([is_contained_boring(one, two) for one, two in pairs])
    return total


def is_contained_boring(one: str, two: str) -> bool:
    if is_contained(one, two) or is_contained(two, one):
        return True
    return False


def is_contained(one: str, two: str) -> bool:
    one_range, two_range = [int(_) for _ in one.split("-")], [
        int(_) for _ in two.split("-")
    ]
    return one_range[0] <= two_range[0] and one_range[1] >= two_range[1]


def find_overlaps(pairs: List[List[str]]) -> int:
    total = sum([is_overlapping(one, two) for one, two in pairs])
    return total


def is_overlapping(one: str, two: str) -> bool:
    one_range, two_range = [int(_) for _ in one.split("-")], [
        int(_) for _ in two.split("-")
    ]
    return (one_range[0] <= two_range[0] and one_range[1] >= two_range[0]) or (
        two_range[0] <= one_range[0] and two_range[1] >= one_range[0]
    )


# print(find_contained_pairs(data))
print(find_contained_pairs_boring(data))
print(find_overlaps(data))
