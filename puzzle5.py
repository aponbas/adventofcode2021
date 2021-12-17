with open("input5.txt", "r") as file:
    data = file.read().splitlines()
import time
vector = []
grid = [[0]*1000]*1000

for line in data:
    coordinates = line.split(" -> ")
    A = coordinates[0].split(",")
    B = coordinates[1].split(",")
    x_1 = int(A[0])
    x_2 = int(B[0])
    y_1 = int(A[1])
    y_2 = int(B[1])

    if x_1 == x_2:
        vector = list(range(min(y_1, y_2), max(y_1, y_2)+1))
        for i in vector:
            grid[x_1][i] += 1
            # print("hierx=x")
            # print(i)
            # print(x_1)
            # print(grid[x_1][i])
            # time.sleep(0.1)
            # print(str(x_1) + "  " + str(i))
    elif y_1 == y_2:
        vector = list(range(min(x_1, x_2), max(x_1, x_2)+1))
        for i in vector:
            grid[y_1][i] += 1
            # print("hiery=y")
            # print(i)
            # print(y_1)
            # print(grid[i][y_1])
            # time.sleep(0.1)
overlap = 0
for i in grid:
    for j in i:
        if j > 1:
            overlap += 1
print(overlap)