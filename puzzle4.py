import numpy

with open("input4.txt", "r") as file:
    data = file.read().splitlines()
ball_list = [int(i) for i in data[0].split(",")]

board_list = []
board = []
for line in data[2:]:
    if line == "":
        board_list.append(board)
        board = []
        continue
    row_to_add = line.split(" ")
    board.append([int(i) for i in row_to_add if i != ""])


def adjust_board(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = -1
    return board


def check_board(board):
    for row in board:
        if sum(row) == -5:
            return True
    return False


def get_value(board):
    value = 0
    for row in board:
        for element in row:
            if element == -1:
                continue
            else:
                value += element
    return value


bingo = {}
for board in board_list:
    roll = 0
    for number in ball_list:
        roll += 1
        board = adjust_board(board)
        transposed_board = numpy.transpose(board).tolist()
        if check_board(board) or check_board(transposed_board):
            value = get_value(board)
            answer = value * number
            bingo[roll] = answer
            break

# Part 1

least_rolls = min(bingo.keys())
score = bingo[least_rolls]
print("puzzle 4a: " + str(score))

# Part 2

most_rolls = max(bingo.keys())
score = bingo[most_rolls]
print("puzzle 4b: " + str(score))