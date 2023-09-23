from tkinter import Frame
import tkinter as tk


class FrameSelectorFrame(Frame) :

    def __init__(self, *args, **kwargs) -> None :

        super().__init__(*args, **kwargs)

        self.header = tk.Label(self, text='HostCommunication Selector')

        self.radioButtonVariable = tk.IntVar()

        self.photowattRadioButton = tk.Radiobutton(self, text='Photowatt Host', variable = self.radioButtonVariable, value=0)
        self.hanwhaRadioButton = tk.Radiobutton(self, text='Hanwha Korea Host', variable = self.radioButtonVariable, value=1)

        self.header.grid(row=0, column=0, padx=5, pady=5)
        self.photowattRadioButton.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.hanwhaRadioButton.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        