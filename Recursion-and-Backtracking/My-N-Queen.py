global N, Row, Colomn, Board
N = 4
Row = [0]*N
Colomn = [0]*N

Board = [[0]*N for i in range(N)]


def printBoard(Board):
    for i in range(N):
        for j in range(N):
            print(Board[i][j], end=" ")
        print()


def solveNQueen(Board, oRow):
    if oRow >= N:
        if 0 not in Row and Colomn:
            return True
        else:
            return False

    for col in range(N):
        if isSafe(Board, oRow, col) is True:
            Board[oRow][col] = 1
            Row[oRow] = 1
            Colomn[col] = 1
            if solveNQueen(Board, oRow+1) is True:
                return True
            Board[oRow][col] = 0
            Row[oRow] = 0
            Colomn[col] = 0


def isSafe(Board, i, j):
    if Row[i] == 1:
        return False
    elif Colomn[j] == 1:
        return False

    for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
        if Board[x][y] == 1:
            return False

    for x, y in zip(range(i, N, 1), range(j, -1, -1)):
        if Board[x][y] == 1:
            return False

    for x, y in zip(range(i, -1, -1), range(j, N, 1)):
        if Board[x][y] == 1:
            return False

    for x, y in zip(range(i, N, 1), range(j, N, 1)):
        if Board[x][y] == 1:
            return False

    return True


if solveNQueen(Board, 0) is True:
    printBoard(Board)
else:
    print(-1)
