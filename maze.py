from cell import Cell
from graphics import Window, Point, Line
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if self.seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                new_cell = Cell(self._win)
                col_cells.append(new_cell)
            self._cells.append(col_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)



    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)

        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j] 
        current_cell.visited = True
        while True:
            to_visit = []
            if (i-1) >= 0 and (i-1) < self.height and j >= 0 and j < self.width:
                north_cell = self._cells[i-1][j]
                if not north_cell.visited:
                    to_visit.append((i-1, j))  
            if (i+1) >= 0 and (i+1) < self.height and j >= 0 and j < self.width:
                south_cell = self._cells[i+1][j]
                if not south_cell.visited:
                    to_visit.append((i+1, j))
            if i >= 0 and i < self.height and (j+1) >= 0 and (j+1) < self.width:
                east_cell = self._cells[i][j+1]
                if not east_cell.visited:
                    to_visit.append((i, j+1))
            if i >= 0 and i < self.height and (j-1) >= 0 and (j-1) < self.width:
                west_cell = self._cells[i][j-1]
                if not west_cell.visited:
                    to_visit.append((i, j-1))

            if len(to_visit) == 0:
                return

            next_index = random.randrange(len(to_visit))
            next_i, next_j = to_visit[next_index]
            
            if next_i == i - 1:  
                current_cell.north_wall = False  
                next_cell = self._cells[next_i][next_j]
                next_cell.south_wall = False    


            elif next_i == i + 1:  # next cell is below current cell
                current_cell.south_wall = False
                next_cell = self._cells[next_i][next_j]
                next_cell.north_wall = False

            elif next_j == j + 1:
                current_cell.east_wall = False
                next_cell = self._cells[next_i][next_j]
                next_cell.west_wall = False
    

            elif next_j == j - 1:
                current_cell.west_wall = False
                next_cell = self._cells[next_i][next_j]
                next_cell.east_wall = False
   
            self._break_walls_r(next_i, next_j)




        




        
        
        
        
        
        
        
            

