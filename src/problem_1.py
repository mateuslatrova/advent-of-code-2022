import sys


def solution_1(input_path):
    input_file = open(input_path)
    count = 0
    calories = [0]

    for line in input_file.readlines():
        if not line.strip():
            count += 1
            calories.append(0)
            continue

        calories[count] += int(line)

    max_calories = max(calories)
    elf = calories.index(max_calories) + 1
    return (max_calories, elf)


if __name__ == "__main__":
    max_calories, elf = solution_1(sys.argv[1])
    print(f"Max calories {max_calories} by elf {elf}")
