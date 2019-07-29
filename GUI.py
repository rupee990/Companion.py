#Main GUI Object

import tkinter as tk
from tkinter import messagebox
import Workspace
import datetime
import TimeManager as tm
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Companion')
        self.root.geometry("500x250")

        #Setup Buttons
        self.ButtonsSetup()

        #Setup Clock
        self.timeFrame = tk.Frame(self.root, bg = "#AFAFAF").pack(fill = 'both')
        self.timelabel = tk.Label(self.timeFrame, text="Hello")
        self.timelabel.pack()
        self.update_clock()
        
        self.root.mainloop()

    def ButtonsSetup(self):
        #Frame for buttons
        self.buttonsFrame = tk.Frame(self.root, width = 312, height = 272.5, bg = "grey")
        self.buttonsFrame.pack(side = "left", fill = 'y')

        #Button which opens the workspace
        self.btnWorkspace = tk.Button(self.buttonsFrame, text = "Open Environment", fg = "black", width = 15, height = 1, command = Workspace.OpenWorkspace).pack()

        #button for time management
        self.btnClockIn = tk.Button(self.buttonsFrame, text = "Clock In", fg = "black", width = 15, height = 1, command = tm.StampStart).pack()
        self.btnClockBreak = tk.Button(self.buttonsFrame, text = "Break", fg = "black", width = 15, height = 1, command = self.GoOnBreak).pack()
        self.btnClockOut = tk.Button(self.buttonsFrame, text = "Clock Out", fg = "black", width = 15, height = 1, command = tm.StampEnd).pack()

    def update_clock(self):
        date = datetime.datetime.now();
        datestring = date.strftime('%Y/%m/%d %H:%M:%S')
        self.timelabel.configure(text=datestring)
        self.root.after(1000, self.update_clock)
        
        
    def GoOnBreak(self):
        tm.StampStartBreak()
    
        if tk.messagebox.showinfo("Breaktime", "Gone on Break!"):   
            tm.StampEndBreak()
        
app = App()


