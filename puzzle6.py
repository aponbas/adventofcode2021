import math

with open("input6.txt", "r") as file:
    data = file.read().split(",")
fishes = [int(i) for i in data]

# for day in range(0, 256):
#     for i in range(0, len(fishes)):
#         fishes[i] -= 1
#         if fishes[i] == -1:
#             fishes[i] = 6
#             fishes.append(8)
#     print(day)
# print(len(fishes))

print(len(fishes))
max_days = 256
new_borns = 0
for day in range(0, max_days):
    for fish in fishes:
        new_borns += math.ceil((max_days-day-fish)/7)
    print(new_borns)
    break
