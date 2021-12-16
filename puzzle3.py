import numpy

with open("input3.txt", "r") as file:
    data = file.read().splitlines()


def transpose(data):
    new_data = []
    for row in data:
        split_row = [int(i) for i in str(row)]
        new_data.append(split_row)
    return numpy.transpose(new_data).tolist()


def find_most_common_bit(row):
    zeros = row.count(0)
    ones = row.count(1)
    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
    else:
        return -1


# Part 1
gamma_rate = ""
epsilon_rate = ""

transposed = transpose(data)
for transposed_column in transposed:
    most_common = find_most_common_bit(transposed_column)
    gamma_rate += str(most_common)
    epsilon_rate += str(1-most_common)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power = gamma_rate * epsilon_rate
print("puzzle 3a: " + str(power))

# Part 2


def get_oxygen(data, index):
    new_data = []
    transposed_column = transpose(data)[index]
    most_common = find_most_common_bit(transposed_column)
    if most_common == -1:
        most_common = 1
    for row in data:
        if int(row[index]) == most_common:
            new_data.append(row)
    if len(new_data) == 1:
        return new_data
    else:
        return get_oxygen(new_data, index + 1)


def get_CO2(data, index):
    new_data = []
    transposed_column = transpose(data)[index]
    most_common = find_most_common_bit(transposed_column)
    if most_common == -1:
        most_common = 1
    for row in data:
        if int(row[index]) == 1 - most_common:
            new_data.append(row)
    if len(new_data) == 1:
        return new_data
    else:
        return get_CO2(new_data, index + 1)


index = 0
oxygen = get_oxygen(data, index)
CO2 = get_CO2(data, index)

oxygen_rate = int(oxygen[0], 2)
CO2_rate = int(CO2[0], 2)
life_support = oxygen_rate * CO2_rate
print("puzzle 3b: " + str(life_support))
