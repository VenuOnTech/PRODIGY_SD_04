import random

def print_board(board):
    for i in range(9):
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def is_valid(board, num, pos):
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):  # Numbers 1-9
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def fill_board(board):
    for i in range(81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            random.shuffle(numbers := list(range(1, 10)))
            for num in numbers:
                if is_valid(board, num, (row, col)):
                    board[row][col] = num
                    if not find_empty(board) or fill_board(board):
                        return True
                    board[row][col] = 0
            break
    return False

def remove_numbers(board, num_holes):
    holes = 0
    while holes < num_holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            holes += 1

def generate_sudoku(num_holes):
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    puzzle = [row[:] for row in board]
    remove_numbers(puzzle, num_holes)
    return puzzle, board

def input_puzzle():
    print("Enter the Sudoku puzzle row by row, use 0 for empty cells:")
    puzzle = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row):
                    raise ValueError("Each row must have exactly 9 numbers between 0 and 9.")
                puzzle.append(row)
                break
            except ValueError as e:
                print(e)
    return puzzle

print("Choose an option:")
print("1. Generate a Sudoku puzzle")
print("2. Input a Sudoku puzzle to solve")

option = int(input("Enter your choice (1/2): "))

if option == 1:
    level = int(input("Enter the level of Sudoku Puzzle (1/2/3/4/5): "))

    if level == 1:
        difficulty = random.randint(20, 25)
    elif level == 2:
        difficulty = random.randint(25, 30)
    elif level == 3:
        difficulty = random.randint(30, 35)
    elif level == 4:
        difficulty = random.randint(35, 40)
    elif level == 5:
        difficulty = random.randint(40, 50)
    else:
        print("Invalid level. Please choose a valid level.")

    puzzle, solution = generate_sudoku(difficulty)

    print("Generated Sudoku Puzzle:")
    print_board(puzzle)

    sol = input("\nDo you want to solve it? (y/n): ")
    if sol.lower() == 'y':
        print("\nSudoku Solution:")
        print_board(solution)
    else:
        print("Exiting...")

elif option == 2:
    puzzle = input_puzzle()
    print("\nInput Sudoku Puzzle:")
    print_board(puzzle)

    if solve(puzzle):
        print("\nSudoku Solution:")
        print_board(puzzle)
    else:
        print("\nNo solution exists for the given puzzle.")

else:
    print("Invalid option. Exiting...")
