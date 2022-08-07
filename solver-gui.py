from pylibui.core import App
from pylibui.controls import Window, VerticalBox, HorizontalBox, Button, Combobox, Label, VerticalSeparator, HorizontalSeparator
import solver

CELL_INFO = []
NUM_LIST = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
CELL_TO_COMPUTE = []
CELL_VALUE = []
CELL_FINISHED = [False for _ in range(81)]

class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()

class ChooseWin(Window):

    def onClose(self, data):
        CELL_INFO.pop()
        CELL_INFO.pop()
        super().onClose(data)

class ChooseCbox(Combobox):

    def onSelected(self, data):
        return self.selected()

class ChooseBtn(Button):

    def onClick(self, data):
        y = CELL_INFO.pop()
        x = CELL_INFO.pop()
        value = canvas.children[0].selected()
        vbox.children[x + int(x / 3) + 1].children[y + int(y / 3) + 1].setText(NUM_LIST[value])
        try:
            index = CELL_TO_COMPUTE.index((x, y))
        except:
            index = len(CELL_TO_COMPUTE)
            CELL_TO_COMPUTE.append((x, y))
            CELL_VALUE.append(value)
        finally:
            if value != 0:
                CELL_VALUE[index] = value
            else:
                CELL_TO_COMPUTE.pop(index)
                CELL_VALUE.pop(index)
        
        choose_window.hide()

class Calculate(Button):

    def onClick(self, data):
        # Freeze UI
        self.setEnabled(False)
        for x in range(9):
            for y in range(9):
                vbox.children[x + int(x / 3) + 1].children[y + int(y / 3) + 1].setEnabled(False)
        # Calculate
        result_index = []
        result_value = []
        for i in range(len(CELL_TO_COMPUTE)):
            CELL_FINISHED[CELL_TO_COMPUTE[i][0] * 9 + CELL_TO_COMPUTE[i][1]] = True
            tmp_index, tmp_value = sudoku_solver.update_table(CELL_TO_COMPUTE[i][0], CELL_TO_COMPUTE[i][1], CELL_VALUE[i])
            result_index.extend(tmp_index)
            result_value.extend(tmp_value)
        if sudoku_solver.unsolved_cell_count > 0:
            tmp_index, tmp_value = sudoku_solver.find_unique_in_part()
            result_index.extend(tmp_index)
            result_value.extend(tmp_value)
        if sudoku_solver.unsolved_cell_count > 0:
            tmp_index, tmp_value = sudoku_solver.search_for_possible_solution()
            result_index.extend(tmp_index)
            result_value.extend(tmp_value)
        # Refresh UI
        for i in range(len(result_index)):
            x = int(result_index[i] / 9)
            y = result_index[i] % 9
            value = result_value[i]
            CELL_FINISHED[result_index[i]] = True
            vbox.children[x + int(x / 3) + 1].children[y + int(y / 3) + 1].setText(str(value))
        for i in range(81):
            x = int(i / 9)
            y = i % 9
            if not CELL_FINISHED[i]:
                vbox.children[x + int(x / 3) + 1].children[y + int(y / 3) + 1].setEnabled(True)
        self.setEnabled(True)
            

class Cell(Button):
    x = 0
    y = 0
    def onClick(self, data):
        CELL_INFO.append(self.x)
        CELL_INFO.append(self.y)
        canvas.children[0].setSelected(0)
        choose_window.show()

app = App()
sudoku_solver = solver.Solver()

window = MyWindow('Sudoku Solver', 450, 400)
window.setMargined(True)

# Main window
vbox = VerticalBox()
vbox.setPadded(True)

for i in range(9):
    if (i % 3) == 0:
        vbox.append(HorizontalSeparator())
    vbox.append(HorizontalBox())
    for j in range(9):
        if (j % 3) == 0:
            vbox.children[i + int(i / 3) + 1].append(Label(" "))
        vbox.children[i + int(i / 3) + 1].append(Cell(" "))
        vbox.children[i + int(i / 3) + 1].children[j + int(j / 3) + 1].x = i
        vbox.children[i + int(i / 3) + 1].children[j + int(j / 3) + 1].y = j

vbox.append(Calculate("Calculate"))
app_info = Label("Version v1.0       https://github.com/lengran/sudoku-solver")
app_info.setEnabled(False)
vbox.append(app_info)

window.setChild(vbox)

# Cell window
choose_window = ChooseWin("Choose Number", 200, 80, False)
canvas = VerticalBox()
canvas.setPadded(True)
canvas.append(ChooseCbox(NUM_LIST))
canvas.append(ChooseBtn("Comfirm"))
choose_window.setChild(canvas)

# Show Main Window
window.show()

app.start()
app.close()
