from typing import List


with open("day2_input.txt") as file:
    guide = [line.split(" ") for line in file.read().split("\n")]

scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
scores_2 = {"X": 0, "Y": 3, "Z": 6}


def calculate_score(opp: str, you: str) -> int:
    score = 0
    if scores[opp] == scores[you]:
        score += 3
    elif scores[you] == scores[opp] % 3 + 1:
        score += 6
    return score + scores[you]


def calculate_score_2(opp: str, result: str) -> int:
    score = 0
    if result == "X":
        score = scores[opp] - 1
        if score == 0:
            score = 3
    elif result == "Y":
        score = scores[opp]
    else:
        score = (scores[opp] % 3) + 1
    print(f"{opp=}, {result=}, {score=}")
    return score + scores_2[result]


def calulcate_total(guide: List[List[str]]) -> int:
    total = 0
    for opp, you in guide:
        total += calculate_score_2(opp, you)
    return total


print(calulcate_total(guide))
