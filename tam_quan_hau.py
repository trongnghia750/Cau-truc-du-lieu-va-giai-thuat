def solveNQueens(n):
    def isSafe(row, col, queens):
        return all(row != i and col != j and row - i != col - j and row - i != j - col
                   for i, j in queens)

    def backtrack(queens, row):
        if row == n:
            result.append(queens)
            return
        for col in range(n):
            if isSafe(row, col, queens):
                backtrack(queens + [(row, col)], row + 1)

    result = []
    backtrack([], 0)
    return result
n = 8
solutions = solveNQueens(n)
for sol in solutions:
    board = []
    for i in range(n):
        row = ['.'] * n
        row[sol[i][1]] = 'Q'
        board.append(''.join(row))
    print(board)