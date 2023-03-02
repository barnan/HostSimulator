from tkinter import Frame
import tkinter as tk

class OtherFrame(Frame) :

    def __init__(self, *args, **kwargs) -> None :

        super().__init__(*args, **kwargs)

        self.label = tk.Label(self, text="Other Frame")

        self.label.pack()

