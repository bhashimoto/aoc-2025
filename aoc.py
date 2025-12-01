import sys

import src


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("arguments needed")
        return
    run(args[0], args[1], args[2])


def run(day: str, problem: str, type: str):
    with open(f"./data/{day}/{type}.txt") as f:
        data = f.readlines()
        data = [line[:-1] for line in data]

        function_name = f"d{day}_{problem}"
        getattr(src, function_name)(data)


if __name__ == "__main__":
    main()
