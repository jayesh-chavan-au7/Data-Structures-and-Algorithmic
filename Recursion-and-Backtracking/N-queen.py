global N, Column, Row
N = 4
Column = [0]*N
Row = [0]*N


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def solveNQueen(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueen(board, col+1) is True:
                return True
            board[i][col] = 0

    return False


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


board = [[0]*N for i in range(N)]

if solveNQueen(board, 0) is True:
    printSolution(board)
else:
    print(-1)
    printSolution(board)
