from tkinter import *
from tkinter.colorchooser import askcolor


class PaintApp:
    def __init__(self):
        root = Tk()

        drawing_area = Canvas(root, bg='white', width=600, height=600)

        self.pen_btn = Button(
            root, text='pen',
            command=self.use_pen)

        self.line_btn = Button(
            root, text='line',
            command=self.use_line)

        self.arc_btn = Button(
            root, text='arc',
            command=self.use_arc)

        self.oval_btn = Button(
            root, text='oval',
            command=self.use_oval)

        self.rect_btn = Button(
            root, text='rectangle',
            command=self.use_rect)

        self.eraser_btn = Button(
            root, text='eraser',
            command=self.use_pen)

        self.color_btn = Button(
            root, text='color',
            command=self.choose_color)

        self.size_selector = Scale(
            root, from_=1, to=10, orient=VERTICAL)

        self.active_btn = self.pen_btn

        self.pen_btn.grid(row=0, column=0)
        self.line_btn.grid(row=1, column=0)
        self.arc_btn.grid(row=2, column=0)
        self.oval_btn.grid(row=3, column=0)
        self.rect_btn.grid(row=4, column=0)
        self.eraser_btn.grid(row=5, column=0)
        self.color_btn.grid(row=6, column=0)
        self.size_selector.grid(row=7, column=0)
        drawing_area.grid(row=0, column=1, rowspan=8)

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_btn_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_btn_up)

        root.mainloop()

    # Stores current drawing tool used
    drawing_tool = "pencil"

    color = "black"

    # Tracks whether left mouse is down
    left_btn = "up"

    # x and y positions for drawing with pencil
    x_pos, y_pos = None, None

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt = None, None
    x2_line_pt, y2_line_pt = None, None

    coords = [None] * 4

    # ---------- CATCH MOUSE DOWN ----------

    def left_btn_down(self, event=None):
        self.left_btn = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # ---------- CATCH MOUSE UP ----------

    def left_btn_up(self, event=None):
        self.left_btn = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        self.coords = [self.x1_line_pt, self.y1_line_pt,
                       self.x2_line_pt, self.y2_line_pt]

        # If mouse is released and line tool is selected
        # draw the line
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "eraser":
            pass

    # ---------- CATCH MOUSE MOVEMENT ----------

    def motion(self, event=None):
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    # ---------- DRAW PENCIL ----------

    def pencil_draw(self, event=None):
        if self.left_btn == "down":
            line_width = self.size_selector.get()

            # Make sure x and y have a value
            if self.x_pos != None and self.y_pos != None:
                event.widget.create_line(
                    self.x_pos, self.y_pos,
                    event.x, event.y,
                    width=line_width, capstyle=ROUND,
                    smooth=TRUE, splinesteps=36,
                    fill=self.color
                )

            self.x_pos = event.x
            self.y_pos = event.y

    # ---------- DRAW LINE ----------

    def line_draw(self, event=None):
        if all(self.coords):
            event.widget.create_line(self.coords, smooth=TRUE, fill=self.color)

    # ---------- DRAW ARC ----------

    def arc_draw(self, event=None):

        # Shortcut way to check if none of these values contain None
        if all(self.coords):
            # start : starting angle for the slice in degrees
            # extent: width of the slice in degrees
            # fill  : fill color if needed
            # style : can be ARC, PIESLICE, or CHORD
            event.widget.create_arc(
                self.coords,
                fill=self.color,
                start=0,
                extent=150,
                style=ARC
            )

    # ---------- DRAW OVAL ----------

    def oval_draw(self, event=None):
        if all(self.coords):

            event.widget.create_oval(
                self.coords,
                fill=self.color,
                outline="black",
                width=2
            )

    # ---------- DRAW RECTANGLE ----------

    def rectangle_draw(self, event=None):
        if all(self.coords):

            # fill : Color option names are here http://wiki.tcl.tk/37701
            # outline : border color
            # width : width of border in pixels

            event.widget.create_rectangle(
                self.coords,
                fill=self.color,
                outline="black",
                width=2
            )

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_pen(self):
        self.drawing_tool = "pencil"
        self.activate_button(self.pen_btn)

    def use_line(self):
        self.drawing_tool = "line"
        self.activate_button(self.line_btn)

    def use_arc(self):
        self.drawing_tool = "arc"
        self.activate_button(self.arc_btn)

    def use_oval(self):
        self.drawing_tool = "oval"
        self.activate_button(self.oval_btn)

    def use_rect(self):
        self.drawing_tool = "rectangle"
        self.activate_button(self.rect_btn)

    def use_eraser(self):
        self.drawing_tool = "pencil"
        self.activate_button(self.pen_btn)

    def activate_button(self, clicked_btn, eraser_mode=False):
        self.active_btn.config(relief=RAISED)
        clicked_btn.config(relief=SUNKEN)
        self.active_btn = clicked_btn
        self.eraser_on = eraser_mode


if __name__ == "__main__":
    PaintApp()
