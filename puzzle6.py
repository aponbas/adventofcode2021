import math

# pascal_dict = {}
# cycle = 0
#
# max_cycles = math.ceil(last_day/)
# for day in range(9, 125):
#     if day % 8 != 0:
#         continue
#     cycle += 1
#     print(day)
#     n = int(day / 8)
#     k_list = range(0, n + 1)
#     pascal = []
#     for k in k_list:
#         x = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
#         pascal.append(x)
#         pascal.append(0)
#     pascal_dict[cycle] = pascal[:-1]
# print(pascal_dict[6])



# with open("input6.txt", "r") as file:
#     data = file.read().split(",")
# fishes = [int(i) for i in data]
new_fish_maturity = 4  # 1 = a new fish requires 1 day before producing offspring
gestation_period = 1  # 0 = every day a new fish
last_day = 20

fishes = [new_fish_maturity]
# This is day 0, we have a fish
calc_state = [1]

# Then starting from the next day
for day in range(1, last_day):
    for i in range(0, len(fishes)):
        fishes[i] -= 1
        if fishes[i] == -1:
            fishes[i] = gestation_period
            fishes.append(new_fish_maturity)
    min_state = max(0, day - new_fish_maturity*2)
    max_state = max(1, day - new_fish_maturity + 1)

    # for ges = 0
    # min_state = max(0, day - new_fish_maturity*2)
    # max_state = max(1, day - new_fish_maturity + 1)
    calc = sum(calc_state[min_state:max_state])
    calc_state.append(calc)
    print("day: " + str(day) + ", calc: " + str(calc) + ", should be: " + str(len(fishes)))
    print(str(min_state) + " " + str(max_state))
    print(calc_state)
    print('\n')
    # print(str(day) + ", " + str(len(fishes)))

# max_days = 256
# new_borns = 0
# for day in range(0, max_days):
#     for fish in fishes:
#         new_borns += math.ceil((max_days-day-fish)/7)
#     print(new_borns)
#     break
