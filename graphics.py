from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.running_window = False

    def draw_line(self, Line, fill_color):
        draw(Line) #this needs to be fixed

class Point:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, Canvas, fill_color):
        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )


    

