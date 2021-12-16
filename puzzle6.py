with open("input6.txt", "r") as file:
    data = file.read().split(",")
fishes = [int(i) for i in data]

for day in range(0, 80):
    for i in range(0, len(fishes)):
        fishes[i] -= 1
        if fishes[i] == -1:
            fishes[i] = 6
            fishes.append(8)
print(len(fishes))
