from pathlib import Path


def main() -> None:
    dir_path = Path(__file__).resolve().parent
    with open(f"{dir_path}/day1_input.txt") as file:
        data = file.read().splitlines()

    print(solution(data))


valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(data: list[str]) -> str:
    total = 0
    for line in data:
        print(line)
        first, last = None, None
        for idx in range(len(line)):
            word_digit = find_word_digit(line[idx:])
            if word_digit:
                word_digit = str(valid_digits.index(word_digit) + 1)
            if not first:
                if line[idx].isdigit():
                    first = line[idx]
                else:
                    first = word_digit
            if line[idx].isdigit():
                last = line[idx]
            else:
                last = word_digit if word_digit else last

        total += int(first + last)
    return total


def find_word_digit(line: str) -> str | None:
    for word in valid_digits:
        if line.find(word) == 0:
            return word
    return None


if __name__ == "__main__":
    main()
