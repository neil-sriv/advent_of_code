from pathlib import Path
from collections import deque
from typing import Any

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day11_input.txt") as file:
    data = file.read().splitlines()

import sys

sys.set_int_max_str_digits(1000000)


class Item:
    lcm = 7 * 19 * 13 * 3 * 2 * 11 * 17 * 5
    ops = {
        0: (lambda x: x * 3),
        1: (lambda x: x * 17),
        2: (lambda x: x + 1),
        3: (lambda x: x + 2),
        4: (lambda x: x * x),
        5: (lambda x: x + 8),
        6: (lambda x: x + 6),
        7: (lambda x: x + 7),
    }

    def __init__(self, worry_level: int) -> None:
        self.worry_level = worry_level

    def exec_operation(self, id: int):
        self.worry_level = self.ops[id](self.worry_level)

    def post_inspect(self):
        self.worry_level //= 3

    def test_and_throw(self, test: int, throw: tuple[int, int]) -> int:
        temp_val = self.worry_level % self.lcm
        # temp_val = self.worry_level
        if temp_val % test == 0:
            return throw[0]
        else:
            return throw[1]

    def __repr__(self) -> str:
        return f"{self.worry_level=}"


class Monkey:
    id_counter = 0

    def __init__(
        self, items: list[Item], operation: str, test: int, throw: tuple[int, int]
    ) -> None:
        self.id = Monkey.id_counter
        Monkey.id_counter += 1
        self.items = items
        self.operation = operation
        self.test = test
        self.throw = throw
        self.inspections = 0

    def inspect_items(self, monkeys: Any):
        # print(f"monke {self.id}")
        for item in self.items:
            # print(item.worry_level, self.operation, end=" ")
            item.exec_operation(self.id)
            # print(item.worry_level)
            # item.post_inspect()
            new_monkey_id = item.test_and_throw(self.test, self.throw)
            # print(f"{item} thrown to {new_monkey_id}")
            monkeys[new_monkey_id].add_item(item)
            self.inspections += 1
        self.items.clear()

    def add_item(self, item: Item):
        self.items.append(item)

    def __repr__(self) -> str:
        return f"Monkey({self.id=}, {self.items=}, {self.operation=}, {self.test=}, {self.throw=}, {self.inspections=})"


def parse_monkeys(input: list[str]) -> deque[Monkey]:
    monkeys = deque()
    for idx in range(0, len(input), 7):
        lines = input[idx : idx + 6]
        items = [Item(int(x)) for x in lines[1].strip().replace(",", "").split(" ")[2:]]
        operation = lines[2].strip().split("= ")[-1]
        test = int(lines[3].strip().split("by ")[-1])
        throw = tuple(int(x.strip().split("monkey ")[-1]) for x in lines[4:6])
        monkeys.append(Monkey(items, operation, test, throw))
    return monkeys


def rounds(monkeys: deque[Monkey]) -> None:
    for _ in range(200):
        go_round(monkeys)


def go_round(monkeys: deque[Monkey]) -> None:
    for monkey in monkeys:
        monkey.inspect_items(monkeys)


def calculate_monkey_business(monkeys: deque[Monkey]) -> int:
    inspections = list(sorted(monkeys, key=lambda x: -1 * x.inspections))
    print([x.inspections for x in monkeys])
    return inspections[0].inspections * inspections[1].inspections


import cProfile

monkeys = parse_monkeys(data)
cProfile.run("rounds(monkeys)")
# rounds(monkeys)
# for monkey in monkeys:
#     print(monkey)
print(calculate_monkey_business(monkeys))
