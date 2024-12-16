# Overview
This Python program provides two key functionalities:  
    -> Generate Sudoku puzzles of different difficulty levels.  
    -> Solve custom Sudoku puzzles provided by the user.  


### Features

Sudoku Puzzle Generation:  
    -> Generates Sudoku puzzles with 5 difficulty levels ranging from Easy to Expert.  
    -> Displays the generated puzzle and its solution.  

Custom Puzzle Solving:
    -> Accepts user-input Sudoku puzzles.  
    -> Validates and solves the puzzle or notifies if unsolvable.  

Input Validation:
    -> Ensures puzzle integrity with proper formatting and solvability.  

### Modules and Libraries Used
random: Used to shuffle numbers and generate random positions for Sudoku puzzle creation.  

### Requirements
Python 3.x  

## How to Use
Run the program:  python sudoku_solver.py  
  
Choose an option:  
    1: Generate a Sudoku puzzle.  
    2: Input your own Sudoku puzzle.  
  
Follow the prompts to interact with the program.  
  
Example Input for Custom Puzzle  
Input each row as space-separated numbers, using 0 for empty cells:  

Row 1: 5 3 0 0 7 0 0 0 0  
Row 2: 6 0 0 1 9 5 0 0 0  
Row 3: 0 9 8 0 0 0 0 6 0  
...  
  
If the puzzle is unsolvable, the program outputs:  No solution exists for the given puzzle.
