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
                return self.answer                          # map needs to be updated
            else:
                return 0                                    # No need to update map

    def __str__(self):
        if self.answer == None:
            return " "
        else:
            return str(self.answer)

class Solver:
    table = []
    unsolved_cell_count = 81

    def __init__(self):
        self.unsolved_cell_count = 81
    
        for _ in range(81):
            self.table.append(Number())

    def _pos(self, x, y):
        return (x * 9 + y)

    def _same_row(self, index):
        x = int(index / 9)
        y = index % 9

        cells = []
        for i in range(9):
            if i != y:
                cells.append(self._pos(x, i))
        return cells

    def _same_col(self, index):
        x = int(index / 9)
        y = index % 9

        cells = []
        for i in range(9):
            if i != x:
                cells.append(self._pos(i, y))
        return cells

    def _same_part(self, index):
        # Note: cells don't contain cells already visited by row or column
        x = int(index / 9)
        y = index % 9

        cells = []
        ver_part = int(x / 3)
        hor_part = int(y / 3)
        for i in range(3 * ver_part, (3 * ver_part + 3)):
            for j in range(3 * hor_part, (3 * hor_part + 3)):
                if i != x and j != y:
                    cells.append(self._pos(i, j))
        return cells

    def update_table(self, x, y, v):
        result_index = []
        result_value = []
        self.table[self._pos(x, y)].set_value(v)
        self.unsolved_cell_count = self.unsolved_cell_count - 1

        cells_need_update = self._same_row(self._pos(x, y)) + self._same_col(self._pos(x, y)) + self._same_part(self._pos(x, y))
        value_to_earse = [v for _ in cells_need_update]

        # Update table
        while len(cells_need_update) != 0:
            index = cells_need_update.pop()
            value = value_to_earse.pop()

            ret = self.table[index].earse(value)

            if ret != 0:
                self.unsolved_cell_count = self.unsolved_cell_count - 1
                tmp_cells_need_update = self._same_row(index) + self._same_col(index) + self._same_part(index)
                tmp_value_to_earse = [ret for _ in tmp_cells_need_update]
                cells_need_update.extend(tmp_cells_need_update)
                value_to_earse.extend(tmp_value_to_earse)
                result_index.append(index)
                result_value.append(ret)
        return result_index, result_value

    def find_unique_in_part(self):
        run_find_unique = True
        result_index = []
        result_value = []
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
                            index = self._pos(x, y)
                            if self.table[index].possibility > 1:
                                indexes.append(index)
                    for i in range(len(indexes)):               # iterate through cells
                        for v in range(9):                      # iterate through 9 possible values
                            if self.table[indexes[i]].values[v] == True and value_checked[v] == False:
                                value_checked[v] = True
                                # if there is no other cells that could be of the same value, then cell index[i] is of the value v
                                found_flag = False
                                for j in range(i + 1, len(indexes)):
                                    if self.table[indexes[j]].values[v] == True:
                                        found_flag = True
                                        break
                                if not found_flag:              # cell index[i] is of value v
                                    x = int(indexes[i] / 9)
                                    y = indexes[i] % 9
                                    value = v + 1
                                    result_index.append(indexes[i])
                                    result_value.append(value)
                                    tmp_index, tmp_value = self.update_table(x, y, value)
                                    result_index.extend(tmp_index)
                                    result_value.extend(tmp_value)
                                    run_find_unique = True      # try find unique again from the beginning, this is a hack like goto
                                    break
                        if run_find_unique == True:
                            break
                    if run_find_unique == True:
                        break
                if run_find_unique == True:
                    break
        return result_index, result_value