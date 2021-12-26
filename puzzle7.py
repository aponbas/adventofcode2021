with open("input7.txt", "r") as file:
    data = file.read().split(",")
data = [int(i) for i in data]

moves_list = list(range(0, max(data)))

# Part 1

fuel_per_move = []
for move in moves_list:
    total_fuel = 0
    for i in data:
        total_fuel += abs(move-i)
    fuel_per_move.append(total_fuel)

print("puzzle 7a: " + str(min(fuel_per_move)))

# Part 2

fuel_per_move = []
for move in moves_list:
    total_fuel = 0
    for i in data:
        move_count = abs(move-i)
        total_fuel += (move_count + move_count*move_count)/2
    fuel_per_move.append(total_fuel)

print("puzzle 7b: " + str(int(min(fuel_per_move))))
