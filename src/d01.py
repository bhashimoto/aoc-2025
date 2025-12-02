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
        raw_clicks = int(row[1:])

        full_turns, clicks = divmod(raw_clicks, 100)
        full_turns = abs(full_turns)

        zeroes += full_turns

        next_position = position + clicks*direction

        if next_position > 99 or next_position == 0:
            print(f"dial {row} crossed 0")
            zeroes += 1
            position = next_position % 100
        elif next_position < 0 and position > 0:
            print(f"dial {row} crossed 0")
            zeroes += 1
            position = next_position % 100
        elif next_position < 0 and position == 0:
            print(f"dial {row} started at 0, no cross")
            position = next_position % 100
        else:
            position = next_position

    print(f"password is: {zeroes}")
