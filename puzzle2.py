with open("input2.txt", "r") as file:
    data = file.read().splitlines()

# Part 1

horizontal = 0
depth = 0
for move in data:
    move = move.split(" ")
    direction = move[0]
    length = int(move[1])
    if direction == "forward":
        horizontal += length
    elif direction == "up":
        depth -= length
    elif direction == "down":
        depth += length

answer = horizontal * depth
print("puzzle 2a: " + str(answer))

# Part 2

horizontal = 0
depth = 0
aim = 0
for move in data:
    move = move.split(" ")
    direction = move[0]
    length = int(move[1])
    if direction == "forward":
        horizontal += length
        depth += aim * length
    elif direction == "up":
        aim -= length
    elif direction == "down":
        aim += length

answer = horizontal * depth
print("puzzle 2b: " + str(answer))
