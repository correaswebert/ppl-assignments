from tkinter import *
from tkinter.colorchooser import askcolor


class PaintApp:
    """Basic paint app functionality"""

    drawing_tool = "pencil"     # current tool being used
    color = "black"             # current color being used
    left_btn = "up"             # state of left click (up or down)

    x_pos, y_pos = None, None   # positions for pencil and eraser

    x1_line_pt, y1_line_pt = None, None  # position of mouse down
    x2_line_pt, y2_line_pt = None, None  # position of mouse up

    coords = [None] * 4         # list of [x1, y1, x2, y2]

    width = height = 600        # dimensions of the Canvas

    def __init__(self):
        root = Tk()

        drawing_area = Canvas(root, bg='white',
                              width=self.width, height=self.height)

        self.pen_btn = Button(
            root, text='pen',
            command=self.use_pen)

        self.line_btn = Button(
            root, text='line',
            command=self.use_line)

        self.oval_btn = Button(
            root, text='oval',
            command=self.use_oval)

        self.rect_btn = Button(
            root, text='rectangle',
            command=self.use_rect)

        self.eraser_btn = Button(
            root, text='eraser',
            command=self.use_eraser)

        self.color_btn = Button(
            root, text='color',
            command=self.choose_color)

        self.size_selector = Scale(
            root, from_=1, to=10, orient=VERTICAL)

        # default tool is pencil
        self.active_btn = self.pen_btn

        # allocate the positions of elements
        self.pen_btn.grid(row=0, column=0)
        self.line_btn.grid(row=1, column=0)
        self.oval_btn.grid(row=2, column=0)
        self.rect_btn.grid(row=3, column=0)
        self.eraser_btn.grid(row=4, column=0)
        self.color_btn.grid(row=5, column=0)
        self.size_selector.grid(row=6, column=0)
        drawing_area.grid(row=0, column=1, rowspan=7)

        # bind the events to detect them
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_btn_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_btn_up)

        root.mainloop()

    def left_btn_down(self, event=None):
        """mouse down event"""

        self.left_btn = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def left_btn_up(self, event=None):
        """mouse up event"""

        self.left_btn = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        self.coords = [self.x1_line_pt, self.y1_line_pt,
                       self.x2_line_pt, self.y2_line_pt]

        # use appropriate drawing tool
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)

    def motion(self, event=None):
        """capture continuous mouse motion for pencil and eraser"""

        if self.drawing_tool == "pencil":
            self.pencil_draw(event)
        elif self.drawing_tool == "eraser":
            self.eraser_mode(event)

    def pencil_draw(self, event=None):
        """method to draw continous dots"""

        if self.left_btn == "down":
            line_width = self.size_selector.get()

            # Make sure x and y have a value
            if self.x_pos and self.y_pos:
                event.widget.create_line(
                    self.x_pos, self.y_pos,
                    event.x, event.y,
                    width=line_width, capstyle=ROUND,
                    smooth=TRUE, splinesteps=36,
                    fill=self.color
                )

            self.x_pos = event.x
            self.y_pos = event.y

    def eraser_mode(self, event=None):
        """method to draw continuous white rectangles"""

        if self.left_btn == "down":
            size = self.size_selector.get()

            # Make sure x and y have a value
            if self.x_pos and self.y_pos:
                coords = [
                    max(0, self.x_pos - size),
                    max(0, self.y_pos - size),
                    min(self.width, self.x_pos + size),
                    min(self.height, self.y_pos + size),
                ]

                event.widget.create_rectangle(
                    coords,
                    fill="white",
                    outline="white",
                    width=1
                )

            self.x_pos = event.x
            self.y_pos = event.y

    def line_draw(self, event=None):
        """draw line from (x1, y1) to (x2, y2)"""

        if all(self.coords):
            event.widget.create_line(self.coords, smooth=TRUE, fill=self.color)

    def oval_draw(self, event=None):
        """draw oval with encompassing rectangle from (x1, y1) to (x2, y2)"""

        if all(self.coords):
            event.widget.create_oval(
                self.coords,
                fill=self.color,
                outline="black",
                width=2
            )

    def rectangle_draw(self, event=None):
        """draw rectangle from (x1, y1) to (x2, y2)"""

        if all(self.coords):
            event.widget.create_rectangle(
                self.coords,
                fill=self.color,
                outline="black",
                width=2
            )

    def choose_color(self):
        """ask user to input a color - using sliders or input box"""

        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    # --------------- methods to handle visuals of button clicks ---------------
    def use_pen(self):
        self.drawing_tool = "pencil"
        self.activate_button(self.pen_btn)

    def use_line(self):
        self.drawing_tool = "line"
        self.activate_button(self.line_btn)

    def use_oval(self):
        self.drawing_tool = "oval"
        self.activate_button(self.oval_btn)

    def use_rect(self):
        self.drawing_tool = "rectangle"
        self.activate_button(self.rect_btn)

    def use_eraser(self):
        self.drawing_tool = "eraser"
        self.activate_button(self.eraser_btn)

    def activate_button(self, clicked_btn):
        """sink the clicked button, and raise the previous button"""

        self.active_btn.config(relief=RAISED)
        clicked_btn.config(relief=SUNKEN)
        self.active_btn = clicked_btn


if __name__ == "__main__":
    PaintApp()
