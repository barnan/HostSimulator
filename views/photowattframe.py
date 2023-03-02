import tkinter as tk
from tkinter import *

class PhotowattFrame(Frame) :
    
    def __init__(self, *args, **kwargs) -> None :
        
        super().__init__(*args, **kwargs)

        self.header = tk.Label(self, text='Photowatt Host')

        self.port_number = tk.IntVar(self, 10001)
        self.host_address = tk.StringVar(self, 'localhost')
        self.message = tk.StringVar(self, '')
        self.batchId = tk.IntVar(self, 300)
        self.theoreticalCounter = tk.IntVar(self, 301)
        self.singulationCounter = tk.IntVar(self, 302)
        self.sentTextMessage = tk.StringVar(self, '')

        self.startServerButton = tk.Button(self, text="Start Server", width=10, state=NORMAL)
        self.stopServerButton = tk.Button(self, text="Stop Server", width=10, state=DISABLED)
        self.changeMessageButton = tk.Button(self, text="Change Message", width=15, state=NORMAL)

        self.host_addressEntry = tk.Entry(self, textvariable=self.host_address, width=10, state=NORMAL)
        self.portEntry = tk.Entry(self, textvariable=self.port_number, width=10, state=NORMAL)
        self.batchIdEntry = tk.Entry(self, textvariable=self.batchId, width=10, state=NORMAL)
        self.theoreticalCounterEntry = tk.Entry(self, textvariable=self.theoreticalCounter, width=10, state=NORMAL)
        self.singulationCounterEntry =  tk.Entry(self, textvariable=self.singulationCounter, width=10, state=NORMAL)
        self.sentMessageEntry =  tk.Entry(self, textvariable=self.sentTextMessage, width=50, state=DISABLED)

        self.portLabel = tk.Label(self, text="Server address")
        self.batchIdLabel = tk.Label(self, text="BatchID")
        self.theoreticalCounterLabel = tk.Label(self, text="Theoretical Counter")
        self.singulationCounterLabel = tk.Label(self, text="Singulation Counter")
        self.sentMessageLabel = tk.Label(self, text="Sent Message")


        self.startServerButton.grid(row=0, column=1, padx=5, pady=5)
        self.stopServerButton.grid(row=0, column=2, padx=5, pady=5)
        self.changeMessageButton.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        self.portLabel.grid(row=1, column=0, padx=5, pady=5)
        self.host_addressEntry.grid(row=1, column=1, padx=5, pady=5)
        self.portEntry.grid(row=1, column=2, padx=5, pady=5)

        self.batchIdLabel.grid(row=2, column=0, padx=5, pady=5)
        self.batchIdEntry.grid(row=2, column=1, padx=5, pady=5)

        self.theoreticalCounterLabel.grid(row=3, column=0, padx=5, pady=5)
        self.theoreticalCounterEntry.grid(row=3, column=1, padx=5, pady=5)

        self.singulationCounterLabel.grid(row=4, column=0, padx=5, pady=5)
        self.singulationCounterEntry.grid(row=4, column=1, padx=5, pady=5)

        self.sentMessageLabel.grid(row=6, column=0, padx=5, pady=5)
        self.sentMessageEntry.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # self.protocol("WM_DELETE_WINDOW", MainWindow_OnClosing)
