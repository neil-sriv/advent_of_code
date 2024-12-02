#!/bin/python
import sys
from pathlib import Path


def get_question():
    dir_path = Path(__file__).resolve().parent
    filename = f"{dir_path}/day{sys.argv[1]}_question.txt"
    with open(filename) as file:
        data = file.read()
    question = data[data.find("---") : data.find("Answer:")]
    # if data.find("--- Part Two ---") != -1:
    # question += data[data.find("--- Part Two ---") :]
    with open(filename, "w") as file:
        file.write(question)


if __name__ == "__main__":
    get_question()
