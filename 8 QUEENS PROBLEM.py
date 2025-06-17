def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 'Q':
            return False
    return True
def solve_n_queens(board, row, n):
    if row == n:
        return True 
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = '.'  # Backtrack
    return False
def print_board(board):
    for row in board:
        print(" ".join(row))
def main():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        if rows != cols:
            print("For N-Queens problem, rows and columns must be equal.")
            return
        n = rows
        board = [['.' for _ in range(n)] for _ in range(n)]
        if solve_n_queens(board, 0, n):
            print("\nOne solution to the", n, "Queens problem:")
            print_board(board)
        else:
            print("No solution exists for", n, "Queens.")
    except ValueError:
        print("Invalid input. Please enter integers.")
main()
