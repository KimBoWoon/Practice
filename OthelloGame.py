__author__ = '보운'


def a1(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x][y + 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a1(boards, x, y + 1, stone):
            boards[x][y] = stone


def a2(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x + 1][y + 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a2(boards, x + 1, y + 1, stone):
            boards[x][y] = stone


def a3(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x + 1][y] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a3(boards, x + 1, y, stone):
            boards[x][y] = stone


def a4(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x + 1][y - 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a4(boards, x + 1, y - 1, stone):
            boards[x][y] = stone


def a5(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x][y - 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a5(boards, x, y - 1, stone):
            boards[x][y] = stone


def a6(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x - 1][y - 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a6(boards, x - 1, y - 1, stone):
            boards[x][y] = stone


def a7(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x - 1][y] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a7(boards, x - 1, y, stone):
            boards[x][y] = stone


def a8(boards, x, y, stone):
    if x < 8 and y < 8:
        if boards[x - 1][y + 1] == stone:
            return False
        if boards[x][y] == stone:
            return True
        if a8(boards, x - 1, y + 1, stone):
            boards[x][y] = stone


for t in range(int(input())):
    board = [['+' for y in range(9)] for x in range(9)]

    board[3][3] = board[4][4] = 'O'
    board[3][4] = board[4][3] = 'X'

    for play in range(int(input())):
        pos = input().split()

        if play % 2 == 0:
            if board[int(pos[0]) - 1][int(pos[1])] != 'X' and board[int(pos[0])][int(pos[1])] != 'X' and board[int(pos[0])][int(pos[1]) - 1] != 'X' and board[int(pos[0]) + 1][int(pos[1]) - 2] != 'X' and board[int(pos[0]) - 1][int(pos[1]) - 2] != 'X' and board[int(pos[0]) - 2][int(pos[1]) - 2] != 'X' and board[int(pos[0]) - 2][int(pos[1]) - 1] != 'X' and board[int(pos[0]) - 2][int(pos[1])] != 'X':
                a1(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a2(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a3(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a4(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a5(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a6(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a7(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
                a8(board, int(pos[0]) - 1, int(pos[1]) - 1, 'X')
        else:
            if board[int(pos[0]) - 1][int(pos[1])] != 'O' and board[int(pos[0])][int(pos[1])] != 'O' and board[int(pos[0])][int(pos[1]) - 1] != 'O' and board[int(pos[0]) + 1][int(pos[1]) - 2] != 'O' and board[int(pos[0]) - 1][int(pos[1]) - 2] != 'O' and board[int(pos[0]) - 2][int(pos[1]) - 2] != 'O' and board[int(pos[0]) - 2][int(pos[1]) - 1] != 'O' and board[int(pos[0]) - 2][int(pos[1])] != 'O':
                a1(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a2(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a3(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a4(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a5(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a6(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a7(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')
                a8(board, int(pos[0]) - 1, int(pos[1]) - 1, 'O')

    for row in range(1, 8):
        for col in range(1, 8):
            print(board[row][col], end='')
        print()
