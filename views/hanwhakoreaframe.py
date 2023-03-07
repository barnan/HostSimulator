from tkinter import Frame
import tkinter as tk

class HanwhaKoreaFrame(Frame) :

    def __init__(self, *args, **kwargs) -> None :

        super().__init__(*args, **kwargs)

        self.label = tk.Label(self, text="Hanwha Korea Frame")

        self.label.pack()

