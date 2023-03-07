import tkinter as tk
from .observableview import ObservableView
from .photowattframe import PhotowattFrame
from .rootwindow import RootWindow
from .frameselectorframe import FrameSelectorFrame
from .hanwhakoreaframe import HanwhaKoreaFrame


class View(ObservableView):

    def __init__(self) -> None :
        super().__init__()
        self.root = RootWindow()
        self.frames = {}
        self.current_frame_index = -1

        self.frameselector = FrameSelectorFrame(self.root, highlightbackground="black", highlightthickness=1)
        self.frameselector.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.frameselector.tkraise()

        self.add_frame(PhotowattFrame, 'PhotowattHostFrame')
        self.add_frame(HanwhaKoreaFrame, 'HanwhaKoreaFrame')        
        
        self.root.protocol("WM_DELETE_WINDOW", self.mainwindow_onclosing)
        self.root.after(500, self.after_startup)


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


    def mainwindow_onclosing(self) -> None :
        self.trigger_event('mainwindow_onclosing')


    def destroyroot(self) -> None :
        self.root.destroy()


    def after_startup(self) -> None :
        self.trigger_event('after_startup')
        