with open("input5.txt", "r") as file:
    data = file.read().splitlines()


def count_overlap(data, diagonal=False):
    def get_coordinates(row):
        coordinates = row.split(" -> ")
        x_1, y_1 = coordinates[0].split(",")
        x_2, y_2 = coordinates[1].split(",")

        x_1 = int(x_1)
        y_1 = int(y_1)
        x_2 = int(x_2)
        y_2 = int(y_2)
        return x_1, y_1, x_2, y_2

    def create_list(i, j):
        if i > j:
            li = list(range(i, j-1, -1))
        else:
            li = list(range(i, j+1))
        return li

    def count_grid(grid):
        overlap = 0
        for row in grid:
            overlap += len(row)-row.count(0)-row.count(1)
        return overlap

    grid_size = 1000
    grid = [[0] * grid_size for i in range(grid_size)]

    for row in data:
        x_1, y_1, x_2, y_2 = get_coordinates(row)

        x_length = abs(x_1 - x_2) + 1
        y_length = abs(y_1 - y_2) + 1

        # If the line is a diagonal
        if x_length == y_length:
            # And if a diagonal should be added
            if diagonal:
                x_length = 1
                y_length = 1
            # Else skip adding the diagonal
            else:
                continue

        x_vector = create_list(x_1, x_2) * y_length
        y_vector = create_list(y_1, y_2) * x_length

        for x, y in zip(x_vector, y_vector):
            grid[y][x] += 1

    overlap = count_grid(grid)
    return overlap


# Part 1

print("puzzle 5a: " + str(count_overlap(data)))

# Part 2

print("puzzle 5b: " + str(count_overlap(data, True)))
