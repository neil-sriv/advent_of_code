from pathlib import Path
from typing import Any, Optional, Union
from collections import deque
from pprint import pprint

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day13_input.txt") as file:
    data = [pair.split("\n") for pair in file.read().split("\n\n")]


def parse_lists(input: list[list[str]]) -> deque[Any]:
    pairs = deque()
    for left, right in input:
        pairs.append((parse_nested_list(left), parse_nested_list(right)))
    return pairs


def parse_nested_list(l: str, idx: int = 0) -> deque[Any]:
    stack = deque()
    while idx < len(l):
        c = l[idx]
        if c == ",":
            idx += 1
            continue
        if c != "]":
            if c.isnumeric():
                c = int(c)
            stack.append(c)
        else:
            curr_list = deque()
            val = stack.pop()
            while val != "[":
                curr_list.append(val)
                val = stack.pop()
            stack.append(deque(reversed(curr_list)))
        idx += 1
    return stack.pop()


def compairs(pairs: deque[Any]) -> int:
    correct = list()
    for idx, (left, right) in enumerate(pairs):
        print(f"checking {idx+1}")
        print(f"{left=}, {right=}")

        if compair(left, right, final=True):
            print(f"{idx+1} is ordered")
            print(left, right)
            correct.append(idx + 1)
    print(correct)
    return sum(correct)


def compair(left: deque[Any], right: deque[Any], final: bool = False) -> Optional[bool]:
    print(f"compair {left, right, final}")
    while left and right:
        l_val = left.popleft()
        r_val = right.popleft()
        print(l_val, r_val)
        # print(left, right)

        check = check_values(l_val, r_val)
        if check is not None:
            return check
    if final:
        if len(left) == 0:
            return True
        elif len(right) == 0:
            return False
    return None


def check_values(
    l_val: Union[deque[Any], int], r_val: Union[deque[Any], int]
) -> Optional[bool]:
    print(f"check {l_val=} vs {r_val=}")
    if isinstance(l_val, int) and isinstance(r_val, int):
        if l_val < r_val:
            return True
        elif l_val > r_val:
            return False
    elif isinstance(r_val, int):
        r_val = deque([r_val])
        return check_values(l_val, r_val)
    elif isinstance(l_val, int):
        l_val = deque([l_val])
        return check_values(l_val, r_val)
    elif isinstance(l_val, deque) and isinstance(r_val, deque):
        return compair(l_val, r_val)
    # print("returning None")


pairs = parse_lists(data)
# for left, right in pairs:
#     pprint(left)
#     pprint(right)
#     print()

total = compairs(pairs)
print(total)
