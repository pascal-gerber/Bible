import tkinter as tk
import sys

def calibrate():
    root = tk.Tk()

    SCwidth = root.winfo_screenwidth()
    SCheigt = root.winfo_screenheight()

    Screensize = ([SCwidth, SCheigt])
    root.destroy()
    return(Screensize)

def adapt(size):
    OS = sys.platform
    if OS == "linux":
        return(calibrate()[0]//200)
    else:
        return(size)

