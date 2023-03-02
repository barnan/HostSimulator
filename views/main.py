import tkinter as tk
from .photowattframe import PhotowattFrame
from .rootwindow import RootWindow
from .frameselectorframe import FrameSelectorFrame
from .otherframe import OtherFrame

class View :

    def __init__(self) -> None :
        self.root = RootWindow()
        self.frames = {}
        self.current_frame_index = -1
        self.previous_frame = None

        self.frameselector = FrameSelectorFrame(self.root, highlightbackground="black", highlightthickness=1)
        self.frameselector.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.frameselector.tkraise()

        self.add_frame(OtherFrame, 'OtherFrame')
        self.add_frame(PhotowattFrame, 'PhotowattHostFrame')
        

    def add_frame (self, frame:tk.Frame, name:str) -> None :
        self.frames[name] = frame(self.root, highlightbackground="black", highlightthickness=1)
        self.frames[name].grid(row=0, column=1, padx=10, pady=10, sticky='nsew')


    def switch_frame(self, newIndex:int) -> None : 

        if self.current_frame_index == newIndex :
            return

        frame = list(self.frames.values())[newIndex]
        frame.tkraise()
        self.current_frame_index = newIndex


    def start_mainloop(self) -> None :
        self.root.mainloop()

