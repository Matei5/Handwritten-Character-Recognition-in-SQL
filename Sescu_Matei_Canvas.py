import tkinter as tk

class SingleStrokeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw a Letter!")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.coordinates = []
        self.drawing = False
        self.stroke_segments = []

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_drawing)

    def start_drawing(self, event):
        self.drawing = True
        self.coordinates = [(event.x, event.y)]
        self.start_point = (event.x, event.y)
        for segment_id in self.stroke_segments:
            self.canvas.delete(segment_id)
        self.stroke_segments = []

    def draw(self, event):
        if self.drawing:
            x0, y0 = self.coordinates[-1]
            self.end_point = (event.x, event.y)
            segment_id = self.canvas.create_line(x0, y0, event.x, event.y, fill="black", width=1)
            self.stroke_segments.append(segment_id)
            self.coordinates.append((event.x, event.y))

    def end_drawing(self, event):
        if self.drawing:
            self.drawing = False

            values = "INSERT INTO coords VALUES "
            for cnt, (x,y) in enumerate(self.coordinates):
                values = values +f"({cnt}, {x}, {y}), "
            values = values[:-2] + ";"
            print(values, end="\n\n")

root = tk.Tk()
app = SingleStrokeDrawer(root)
root.mainloop()
