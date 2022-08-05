import os

UNSOLVED_CELL_COUNT = [81]

class Number:
    def __init__(self):
        # self.pos_x = x
        # self.pos_y = y
        self.answer = None
        self.possibility = 9
        self.values = [True, True, True, True, True, True, True, True, True]

    def set_value(self, v):
        self.answer = v
        self.possibility = 1
        UNSOLVED_CELL_COUNT[0] = UNSOLVED_CELL_COUNT[0] - 1
        for i in range(9):
            self.values[i] = False
        self.values[v - 1] = True
    
    def earse(self, v):
        if self.values[v - 1] == False:
            return 0                                        # No need to update map
        else:
            self.values[v - 1] = False
            self.possibility = self.possibility - 1
            if self.possibility == 1:
                for i in range(9):
                    if self.values[i] == True:
                        self.answer =  i + 1
                UNSOLVED_CELL_COUNT[0] = UNSOLVED_CELL_COUNT[0] - 1
                return self.answer                          # map needs to be updated
            else:
                return 0                                    # No need to update map

    def __str__(self):
        if self.answer == None:
            return " "
        else:
            return str(self.answer)

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

def same_row(index):
    x = int(index / 9)
    y = index % 9

    cells = []
    for i in range(9):
        if i != y:
            cells.append(pos(x, i))
    return cells

def same_col(index):
    x = int(index / 9)
    y = index % 9

    cells = []
    for i in range(9):
        if i != x:
            cells.append(pos(i, y))
    return cells

def same_part(index):
    # Note: cells don't contain cells already visited by row or column
    x = int(index / 9)
    y = index % 9

    cells = []
    ver_part = int(x / 3)
    hor_part = int(y / 3)
    for i in range(3 * ver_part, (3 * ver_part + 3)):
        for j in range(3 * hor_part, (3 * hor_part + 3)):
            if i != x and j != y:
                cells.append(pos(i, j))
    return cells

def update_map(table, x, y, v):
    table[pos(x, y)].set_value(v)
    
    cells_need_update = same_row(pos(x, y)) + same_col(pos(x, y)) + same_part(pos(x, y))
    value_to_earse = [v for _ in cells_need_update]

    # Update map
    while len(cells_need_update) != 0:
        index = cells_need_update.pop()
        value = value_to_earse.pop()
        
        ret = table[index].earse(value)

        if ret != 0:
            tmp_cells_need_update = same_row(index) + same_col(index) + same_part(index)
            tmp_value_to_earse = [ret for _ in tmp_cells_need_update]
            cells_need_update.extend(tmp_cells_need_update)
            value_to_earse.extend(tmp_value_to_earse)

def find_unique_in_part(table):
    run_find_unique = True
    while run_find_unique:
        run_find_unique = False                             # if we can't find unique, no need to find_sunique again
        # run 3 x 3 times, check each local unique cell
        for part_x in range(3):
            for part_y in range(3):
                # Check if there are more than 1 cell can be of the same value
                value_checked = [False, False, False, False, False, False, False, False, False]
                
                # generate a cell index array, for convenience
                indexes = []
                for x in range(3 * part_x, 3 * part_x + 3):
                    for y in range(3 * part_y, 3 * part_y + 3):
                        index = pos(x, y)
                        if table[index].possibility > 1:
                            indexes.append(index)
                for i in range(len(indexes)):               # iterate through cells
                    for v in range(9):                      # iterate through 9 possible values
                        if table[indexes[i]].values[v] == True and value_checked[v] == False:
                            value_checked[v] = True
                            # if there is no other cells that could be of the same value, then cell index[i] is of the value v
                            found_flag = False
                            for j in range(i + 1, len(range)):
                                if table[indexes[j]].values[v] == True:
                                    found_flag = True
                                    break
                            if not found_flag:              # cell index[i] is of value v
                                x = int(indexes[i] / 9)
                                y = indexes[i] % 9
                                value = v + 1
        
                                update_map(table, x, y, value)
                                run_find_unique = True      # try find unique again from the beginning, this is a hack like goto
                                break
                    if run_find_unique == True:
                        break
                if run_find_unique == True:
                    break
            if run_find_unique == True:
                break

if __name__ == "__main__":
    table = []
    
    for _ in range(81):
        table.append(Number())

    while UNSOLVED_CELL_COUNT[0] > 0:
        os.system("clear")
        print_map(table)

        x, y, value = get_input()

        update_map(table, x, y, value)
    
    os.system("clear")
    print_map(table)
