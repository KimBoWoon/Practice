__author__ = '보운'


def right(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if right(boards, x, y + 1, stone):
            boards[x][y] = stone
            return True


def rightAndDown(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if rightAndDown(boards, x + 1, y + 1, stone):
            boards[x][y] = stone
            return True


def down(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if down(boards, x + 1, y, stone):
            boards[x][y] = stone
            return True


def leftAndDown(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if leftAndDown(boards, x + 1, y - 1, stone):
            boards[x][y] = stone
            return True


def left(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if left(boards, x, y - 1, stone):
            boards[x][y] = stone
            return True


def leftAndUp(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if leftAndUp(boards, x - 1, y - 1, stone):
            boards[x][y] = stone
            return True


def up(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if up(boards, x - 1, y, stone):
            boards[x][y] = stone
            return True


def rightAndUp(boards, x, y, stone):
    if 0 <= x <= 8 and 0 <= y <= 8:
        if boards[x][y] == '+':
            return False
        if boards[x][y] == stone:
            return True
        if rightAndUp(boards, x - 1, y + 1, stone):
            boards[x][y] = stone
            return True


def stoneCount(boards):
    block = white = 0

    for x in range(8):
        block += boards[x].count('X')
        white += boards[x].count('O')

    return block, white


def printBoards(boards, block, white):
    print(block, white)
    for row in range(0, 8):
        for col in range(0, 8):
            print(boards[row][col], end='')
        print()


for t in range(int(input())):
    board = [['+' for col in range(9)] for row in range(9)]

    board[3][3] = board[4][4] = 'O'
    board[3][4] = board[4][3] = 'X'

    for play in range(int(input())):
        x, y = input().split()
        x = int(x) - 1
        y = int(y) - 1

        if play % 2 == 0:
            if board[x][y + 1] != 'X':
                right(board, x, y + 1, 'X')
            if board[x + 1][y + 1] != 'X':
                rightAndDown(board, x + 1, y + 1, 'X')
            if board[x + 1][y] != 'X':
                down(board, x + 1, y, 'X')
            if board[x + 1][y - 1] != 'X':
                leftAndDown(board, x + 1, y - 1, 'X')
            if board[x][y - 1] != 'X':
                left(board, x, y - 1, 'X')
            if board[x - 1][y - 1] != 'X':
                leftAndUp(board, x - 1, y - 1, 'X')
            if board[x - 1][y] != 'X':
                up(board, x - 1, y, 'X')
            if board[x - 1][y + 1] != 'X':
                rightAndUp(board, x - 1, y + 1, 'X')

            board[x][y] = 'X'
        else:
            if board[x][y + 1] != 'O':
                right(board, x, y + 1, 'O')
            if board[x + 1][y + 1] != 'O':
                rightAndDown(board, x + 1, y + 1, 'O')
            if board[x + 1][y] != 'O':
                down(board, x + 1, y, 'O')
            if board[x + 1][y - 1] != 'O':
                leftAndDown(board, x + 1, y - 1, 'O')
            if board[x][y - 1] != 'O':
                left(board, x, y - 1, 'O')
            if board[x - 1][y - 1] != 'O':
                leftAndUp(board, x - 1, y - 1, 'O')
            if board[x - 1][y] != 'O':
                up(board, x - 1, y, 'O')
            if board[x - 1][y + 1] != 'O':
                rightAndUp(board, x - 1, y + 1, 'O')

            board[x][y] = 'O'

    block, white = stoneCount(board)

    printBoards(board, block, white)
