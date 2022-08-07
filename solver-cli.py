import os
import solver

def pos(x, y):
    return (x * 9 + y)

def print_map(table):
    print("=========================================")
    i = 0
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 1
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 2
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("=========================================")
    i = 3
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 4
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 5
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("=========================================")
    i = 6
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 7
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("-----------------------------------------")
    i = 8
    print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(str(table[pos(i, 0)]), str(table[pos(i, 1)]), str(table[pos(i, 2)]), str(table[pos(i, 3)]), str(table[pos(i, 4)]), str(table[pos(i, 5)]), str(table[pos(i, 6)]), str(table[pos(i, 7)]), str(table[pos(i, 8)]),))
    print("=========================================")

def get_input():
    str = input("x y value: ")
    str_slice = str.split()
    x = int(str_slice[0]) - 1
    y = int(str_slice[1]) - 1
    value = int(str_slice[2])
    return x, y, value

if __name__ == "__main__":
    sudoku_solver = solver.Solver()
    
    while sudoku_solver.unsolved_cell_count > 0:
        os.system("clear")
        print_map(sudoku_solver.table)
        x, y, value = get_input()

        sudoku_solver.update_table(x, y, value)
        sudoku_solver.find_unique_in_part()
    
    os.system("clear")
    print_map(sudoku_solver.table)
