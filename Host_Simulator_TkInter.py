import tkinter as tk
from tkinter import *
import Photowatt_Host_Side
from tkinter import messagebox

DEFAULT_PORT_NUMBER = 3333
VERSION_NUMBER = 'v1.0'
DEFAULT_MESSAGE = b'\x01\x0c\x04K\x1f\x01\x00\x0b\xac\x00\x00\x9b'

mainwindow = tk.Tk()
mainwindow.title(f'Photowatt Host Simulator {VERSION_NUMBER}')
mainwindow.geometry('360x270')
mainwindow.resizable(False, False)

port_number = tk.IntVar(mainwindow, DEFAULT_PORT_NUMBER)
message = tk.StringVar(mainwindow, DEFAULT_MESSAGE)
batchId = tk.IntVar(mainwindow, 100)
theoreticalCounter = tk.IntVar(mainwindow, 101)
singulationCounter = tk.IntVar(mainwindow, 102)
sentTextMessage = tk.StringVar(mainwindow, "")


def OnStartServer():
    OnChangeMessage()
    Photowatt_Host_Side.StartMessageSending(port_number.get())
    startServerButton['state'] = DISABLED
    stopServerButton['state'] = NORMAL
    portEntry['state'] = DISABLED
    

def OnStopServer() -> None :
    Photowatt_Host_Side.StopMessageSending()
    startServerButton['state'] = NORMAL
    stopServerButton['state'] =  DISABLED
    portEntry['state'] = NORMAL
    return


def OnChangeMessage() -> None :
    result = Photowatt_Host_Side.ChnageMessageToSend(batchId.get(), theoreticalCounter.get(), singulationCounter.get())
    sentTextMessage.set(' '.join(result))
    return
    

def MainWindow_OnClosing() -> None :
    OnStopServer()
    mainwindow.destroy()
    return


def OnAfterStartup() -> None :
    OnChangeMessage()
    return 


startServerButton = tk.Button(mainwindow, text="Start Server", command=OnStartServer, width=10, state=NORMAL)
stopServerButton = tk.Button(mainwindow, text="Stop Server", command=OnStopServer, width=10, state=DISABLED)
changeMessageButton = tk.Button(mainwindow, text="Change Message", command=OnChangeMessage, width=15, state=NORMAL)

portEntry = tk.Entry(mainwindow, text=port_number, width=10, state=NORMAL)
batchIdEntry = tk.Entry(mainwindow, textvariable=batchId, width=10, state=NORMAL)
theoreticalCounterEntry = tk.Entry(mainwindow, textvariable=theoreticalCounter, width=10, state=NORMAL)
singulationCounterEntry =  tk.Entry(mainwindow, textvariable=singulationCounter, width=10, state=NORMAL)
sentMessageEntry =  tk.Entry(mainwindow, textvariable=sentTextMessage, width=50, state=DISABLED)

portLabel = tk.Label(mainwindow, text="Server PortNumber")
batchIdLabel = tk.Label(mainwindow, text="BatchID")
theoreticalCounterLabel = tk.Label(mainwindow, text="Theoretical Counter")
singulationCounterLabel = tk.Label(mainwindow, text="Singulation Counter")
sentMessageLabel = tk.Label(mainwindow, text="Sent Message")


startServerButton.grid(row=0, column=1, padx=5, pady=5)
stopServerButton.grid(row=0, column=2, padx=5, pady=5)
changeMessageButton.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

portLabel.grid(row=1, column=0, padx=5, pady=5)
portEntry.grid(row=1, column=1, padx=5, pady=5)

batchIdLabel.grid(row=2, column=0, padx=5, pady=5)
batchIdEntry.grid(row=2, column=1, padx=5, pady=5)

theoreticalCounterLabel.grid(row=3, column=0, padx=5, pady=5)
theoreticalCounterEntry.grid(row=3, column=1, padx=5, pady=5)

singulationCounterLabel.grid(row=4, column=0, padx=5, pady=5)
singulationCounterEntry.grid(row=4, column=1, padx=5, pady=5)

sentMessageLabel.grid(row=6, column=0, padx=5)
sentMessageEntry.grid(row=7, column=0, columnspan=3, padx=5)

mainwindow.protocol("WM_DELETE_WINDOW", MainWindow_OnClosing)
mainwindow.after(100, OnAfterStartup)
mainwindow.mainloop()
