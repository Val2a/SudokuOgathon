import DatasetManager


def read_sudoku_board(file_path):
    board = []
    sudoku_file = open(file_path, "r")

    for line in sudoku_file:
        line_separated = line.split(" ")
        board.append([int(num) for num in line_separated])

    sudoku_file.close()
    return board

def sudokuToStr(sudoku_board):
    str_sudoku = ""
    for row in sudoku_board:
        for cell in row:
            if cell != row[0]:
                str_sudoku += " "
            str_sudoku += str(cell)
        if row != sudoku_board[len(sudoku_board)-1]:
            str_sudoku += "\n"
    return str_sudoku

def is_num_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row = (row // 3) * 3
    start_cell = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_cell, start_cell + 3):
            if board[i][j] == num:
                return False

    return True

# Algoritmo backtracking. El sudoku es un
# ejemplo clásico de problema de backtracking.
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Iteramos entre los posibles números
            if board[row][col] == 0:
                for num in range(1, 10):
                    # Si el número es un buen candidato,
                    # hacemos la llamada recursiva.
                    if is_num_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            # Si tras la llamada se consigue resolver,
                            # devolvemos true.

                            return True
                        # Si no, reseteamos la celda.
                        board[row][col] = 0
                # Si no se ha encontrado ningún numero válido para
                # esa celda, debemos hacer backtracking
                return False
    # Si ha ido bien, se resuelve
    return True

def resolve_sudoku_file(file_path):
    sudoku_board = read_sudoku_board(file_path)
    solve_sudoku(sudoku_board)
    return sudokuToStr(sudoku_board)

DatasetManager.resolve_dataset("dataset_path", resolve_sudoku_file)


