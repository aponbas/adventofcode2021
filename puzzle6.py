import math

pascal_dict = {}
cycle = 0

max_cycles = math.ceil(last_day/)
for day in range(9, 125):
    if day % 8 != 0:
        continue
    cycle += 1
    print(day)
    n = int(day / 8)
    k_list = range(0, n + 1)
    pascal = []
    for k in k_list:
        x = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
        pascal.append(x)
        pascal.append(0)
    pascal_dict[cycle] = pascal[:-1]
print(pascal_dict[6])



# with open("input6.txt", "r") as file:
#     data = file.read().split(",")
# fishes = [int(i) for i in data]
# fishes = [8]
# for day in range(0, 200):
#     old_fishes = len(fishes)
#     for i in range(0, len(fishes)):
#         fishes[i] -= 1
#         if fishes[i] == -1:
#             fishes[i] = 6
#             fishes.append(8)
#     # print("day :" + str(day))
#     # print("fishes : " + str(len(fishes)))
#     difference = str(len(fishes)-old_fishes)
#     # print("difference :" + difference)
#     print(str(day), str(len(fishes)), difference)
# print(len(fishes))

# print(len(fishes))
# max_days = 256
# new_borns = 0
# for day in range(0, max_days):
#     for fish in fishes:
#         new_borns += math.ceil((max_days-day-fish)/7)
#     print(new_borns)
#     break
