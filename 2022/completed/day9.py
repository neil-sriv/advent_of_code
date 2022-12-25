from pathlib import Path
from pprint import pprint
from itertools import pairwise

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day9_input.txt") as file:
    data = file.read().splitlines()


def set_up(input: list[str]) -> tuple[list[tuple[str, int]], list[list[str]]]:
    movement = list()
    for direction, number in [line.split(" ") for line in input]:
        movement.append((direction, int(number)))

    mapping = [["_" for x in range(500)] for x in range(500)]

    return movement, mapping


def journey(mapping: list[list[str]], movement: list[tuple[str, int]]) -> int:
    knots = [[250, 250] for _ in range(10)]
    for direction, number in movement:
        for _ in range(number):
            head = knots[0]
            head[0], head[1] = move(mapping, direction, head)
            propogate(knots, mapping)
    return count_t(mapping)


def propogate(knots: list[list[int]], mapping: list[list[str]]):
    for head, tail in pairwise(knots):
        if big_dist(head, tail):
            tail[0], tail[1] = move_t(head, tail)
    tail = knots[-1]
    mapping[tail[0]][tail[1]] = "T"


def move(
    mapping: list[list[str]],
    direction: str,
    h_pos: list[int],
) -> list[int]:
    r, c = h_pos
    match direction:
        case "U":
            r -= 1
        case "D":
            r += 1
        case "L":
            c -= 1
        case "R":
            c += 1
    return [r, c]


def move_t(
    h_pos: list[int],
    t_pos: list[int],
) -> list[int]:
    h_r, h_c = h_pos
    t_r, t_c = t_pos
    if h_r > t_r:
        t_r += 1
    elif h_r < t_r:
        t_r -= 1
    if h_c > t_c:
        t_c += 1
    elif h_c < t_c:
        t_c -= 1
    return [t_r, t_c]


def big_dist(h_pos: list[int], t_pos: list[int]) -> bool:
    return abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1


def count_t(mapping: list[list[str]]) -> int:
    total = 0
    for row in mapping:
        for val in row:
            if val == "T":
                total += 1
    return total


movement, mapping = set_up(data)
total = journey(mapping, movement)
print(total)
