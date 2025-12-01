def d01_01(input: list[str]):
    position = 50
    zeroes = 0
    # left == lower, right == higher
    for row in input:
        direction = 1 if row[0] == 'R' else -1
        clicks = int(row[1:])

        position = (position + direction*clicks) % 100

        if position == 0:
            zeroes += 1

    print(f"password is: {zeroes}")


def d01_02(input: list[str]):
    position = 50
    zeroes = 0

    for row in input:
        direction = 1 if row[0] == 'R' else -1
        clicks = int(row[1:])

        # TODO
    print(f"password is: {zeroes}")
