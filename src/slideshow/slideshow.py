import tkinter as tk
from PIL import Image, ImageTk
import random
import glob


class Slideshow:
    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.mainwin.title('Picture Frame')
        self.mainwin.state('zoomed')

        self.mainwin.configure(bg='yellow')
        self.frame = tk.Frame(mainwin)

        self.frame.place(relheight=0.85, relwidth=0.9, relx=0.05, rely=0.05)


root = tk.Tk()
Slideshow(root)
root.mainloop()
