with open("input1.txt", "r") as file:
    data = file.read().splitlines()
input = [int(i) for i in data]

# Part 1

increased = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increased += 1
print("puzzle 1a: " + str(increased))

# Part 2

increased = 0
for i in range(3, len(input)):
    if input[i] > input[i-3]:
        increased += 1
print("puzzle 1b: " + str(increased))