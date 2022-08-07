import copy

basis_part = [0, 3, 6, 27, 30, 33, 54, 57, 60]
offset = [0, 1, 2, 9, 10, 11, 18, 19, 20]

def pos(x, y):
    return (x * 9 + y)

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

    def _same_row(self, index):
        x = int(index / 9)
        y = index % 9

        cells = []
        for i in range(9):
            if i != y:
                cells.append(x * 9 + i)
        return cells

    def _same_col(self, index):
        x = int(index / 9)
        y = index % 9

        cells = []
        for i in range(9):
            if i != x:
                cells.append(i * 9 + y)
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
                    cells.append(i * 9 + j)
        return cells

    def update_table(self, x, y, v):
        result_index = []
        result_value = []
        self.table[x * 9 + y].set_value(v)
        self.unsolved_cell_count = self.unsolved_cell_count - 1

        cells_need_update = self._same_row(x * 9 + y) + self._same_col(x * 9 + y) + self._same_part(x * 9 + y)
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
        return result_index, result_value                       # calculated indexes and values, to refresh GUI

    def find_unique_in_part(self):
        run_find_unique = True
        result_index = []
        result_value = []
        while run_find_unique:
            run_find_unique = False                             # if we can't find unique, no need to find_unique again
            # run 3 x 3 times, check each local unique cell
            for part_x in range(3):
                for part_y in range(3):
                    # Check if there are more than 1 cell can be of the same value
                    value_checked = [False, False, False, False, False, False, False, False, False]

                    # generate a cell index array, for convenience
                    indexes = []
                    for x in range(3 * part_x, 3 * part_x + 3):
                        for y in range(3 * part_y, 3 * part_y + 3):
                            index = x * 9 + y
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
        return result_index, result_value                       # calculated indexes and values, to refresh GUI

    def check_row_legitmacy(self):
        for x in range(9):
            existed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in range(9):
                if self.table[x * 9 + y].answer != None:
                    existed[self.table[x * 9 + y].answer - 1] = existed[self.table[x * 9 + y].answer - 1] + 1
            for i in range(9):
                if existed[i] > 1:
                    return False
        return True
    
    def check_col_legitmacy(self):
        for y in range(9):
            existed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in range(9):
                if self.table[x * 9 + y].answer != None:
                    existed[self.table[x * 9 + y].answer - 1] = existed[self.table[x * 9 + y].answer - 1] + 1
            for i in range(9):
                if existed[i] > 1:
                    return False
        return True
    
    def check_part_legitmacy(self):
        for part in range(9):
            existed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(9):
                if self.table[basis_part[part] + offset[i]].answer != None:
                    existed[self.table[basis_part[part] + offset[i]].answer - 1] = existed[self.table[basis_part[part] + offset[i]].answer - 1] + 1
            for i in range(9):
                if existed[i] > 1:
                    return False
        return True

    def check_finished(self):
        # Note: This method only test if all cells have answers, don't check their legitmacy
        for x in range(9):
            for y in range(9):
                if self.table[x * 9 + y].answer == None:
                    return False
        return True

    def search_for_possible_solution(self):
        saved_status = []                                       # each record should contain a table and a (x, y) breaking point
        inference_index = []                                    # updated indexes after each choice
        inference_value = []
        
        while True:
            # First count unsolved cells by row, col, and part
            row = []
            col = []
            part = []
            for x in range(9):
                count = 0
                for y in range(9):
                    if self.table[x * 9 + y].answer == None:
                        count = count + 1
                row.append(count)
            for y in range(9):
                count = 0
                for x in range(9):
                    if self.table[x * 9 + y].answer == None:
                        count = count + 1
                col.append(count)
            for i in range(9):
                count = 0
                for j in range(9):
                    if self.table[basis_part[i] + offset[j]].answer == None:
                        count = count + 1
                part.append(count)
            
            # Iterate each cell to find the most "importent" cell
            index = None
            importance = 0
            for x in range(9):
                for y in range(9):
                    if self.table[x * 9 + y].answer != None:
                        continue
                    if (row[x] + col[y] + part[int(x / 3) + int(y / 3)]) > importance:
                        index = x * 9 + y
                        importance = row[x] + col[y] + part[int(x / 3) + int(y / 3)]
            if index == None:
                raise RuntimeError()
            
            # find the possible value that is most important
            x = int(index / 9)
            y = index % 9
            possible_value = []
            possible_value_count = {}
            for i in range(9):
                if self.table[index].values[i] == True:
                    possible_value.append(i)
                    possible_value_count[i] = 0
            # if there's no possible value for the selected cell, it means that we should step backward, last searching step is wrong
            if len(possible_value) == 0:
                self.unsolved_cell_count = self.unsolved_cell_count + 1
                inference_index.pop()
                inference_index.pop()
                inference_value.pop()
                inference_value.pop()
                record_frame = saved_status.pop()
                self.table = record_frame[0]
                self.table[record_frame[1]].values[record_frame[2]] = False
                self.table[record_frame[1]].possibility = self.table[record_frame[1]].possibility - 1
                continue
            for i in possible_value:
                for j in range(9):
                    if self.table[x * 9 + j].values[i] == True:
                        possible_value_count[i] = possible_value_count[i] + 1
                for j in range(9):
                    if self.table[j * 9 + y].values[i] == True:
                        possible_value_count[i] = possible_value_count[i] + 1
                basis = int(x / 3) * 27 + int(y / 3) * 3
                for j in range(9):
                    if self.table[basis + offset[j]].values[i] == True:
                        possible_value_count[i] = possible_value_count[i] + 1
            choice = possible_value[0]
            choice_count = 0
            for i in range(len(possible_value)):
                if possible_value_count[possible_value[i]] > choice_count:
                    choice = possible_value[i]
                    choice_count = possible_value_count[possible_value[i]]
            
            # Record current status and the choice we made.
            saved_status.append((copy.deepcopy(self.table), index, choice))

            # Do inference
            self.unsolved_cell_count = self.unsolved_cell_count - 1
            tmp_index, tmp_value = self.update_table(x, y, choice + 1)
            inference_index.append(tmp_index)
            inference_value.append(tmp_value)
            tmp_index, tmp_value = self.find_unique_in_part()
            inference_index.append(tmp_index)
            inference_value.append(tmp_value)
            if self.check_row_legitmacy() and self.check_col_legitmacy() and self.check_part_legitmacy():
                if self.check_finished():
                    result_index = []
                    result_value = []
                    for i in range(len(inference_index)):
                        result_index.extend(inference_index[i])
                        result_value.extend(inference_value[i])
                    tmp_index = []
                    tmp_value = []
                    for i in saved_status:
                        tmp_index.append(i[1])
                        tmp_value.append(i[2] + 1)
                    result_index.extend(tmp_index)
                    result_value.extend(tmp_value)
                    return result_index, result_value
                # else, go for another inference step and make next choice
            else:
                if True:
                # while len(saved_status) > 0:
                    # the choice we just made is not legit, step backward and set the choosen value to false
                    self.unsolved_cell_count = self.unsolved_cell_count + 1
                    inference_index.pop()
                    inference_index.pop()
                    inference_value.pop()
                    inference_value.pop()
                    record_frame = saved_status.pop()
                    self.table = record_frame[0]
                    self.table[record_frame[1]].values[record_frame[2]] = False
                    self.table[record_frame[1]].possibility = self.table[record_frame[1]].possibility - 1