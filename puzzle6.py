with open("input6.txt", "r") as file:
    data = file.read().split(",")
fish = [int(i) for i in data]


def counting_offspring(maturity, gestation_period, last_day, fish):
    # This is day 0, we have 1 fish
    fish_count = [1]

    # Then starting from the next day
    final_day = last_day + maturity  # At the end we want to "delay" for fish who are further along their gestation.
    for day in range(1, final_day):
        first_index = day-maturity-1
        second_index = day-gestation_period-1
        if first_index < 0:
            new_fish = 1
        else:
            new_fish = fish_count[first_index] + fish_count[second_index]
        fish_count.append(new_fish)

    # We don't calculate for every fish individually, we just count how many fish of a certain state exist and multiply
    # by the number of fish one of them would produce.
    possible_states = set(fish)
    final_count = 0
    for initial_state in possible_states:
        number_of_fish = fish.count(initial_state)  # The number of fish in the input with that initial state
        offspring = fish_count[final_day - initial_state]  # The total offspring of 1 of those fish
        final_count += number_of_fish * offspring
    return final_count


# Part 1

maturity = 8  # 1 = a new fish requires 1 day before producing offspring.
gestation_period = 6  # 0 = every day a new fish.
last_day = 80  # You want to know how many fish there are after this day.

final_count = counting_offspring(maturity, gestation_period, last_day, fish)
print("puzzle 6a: " + str(final_count))

# Part 2

maturity = 8  # 1 = a new fish requires 1 day before producing offspring.
gestation_period = 6  # 0 = every day a new fish.
last_day = 256  # You want to know how many fish there are after this day.

final_count = counting_offspring(maturity, gestation_period, last_day, fish)
print("puzzle 6b: " + str(final_count))
