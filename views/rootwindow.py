from tkinter import Tk

_VERSION_NUMBER = 2.0

class RootWindow(Tk) :
    
    def __init__(self) :
        super().__init__()

        width = 550
        height = 400

        self.geometry(f'{width}x{height}')
        self.title(f'Host Simulator {str(_VERSION_NUMBER)}')
        self.resizable(False, False)

        
