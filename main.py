from tkinter import *
from tkinter import messagebox
import win32gui
import win32con
import ctypes
import time
import os

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

x = y = 0
hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 

def virus(x, y):
    while True:
        win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_WARNING))
        x = x + 30
        if x >= w:
            y = y + 30
            x = 0
        if y >= h:
            x = y = 0
        win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR))
        x = x + 30
        if x >= w:
            y = y + 30
            x = 0
        if y >= h:
            x = y = 0
        win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_INFORMATION))
        x = x + 30
        if x >= w:
            y = y + 30
            x = 0
        if y >= h:
            x = y = 0
        win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_QUESTION))
        x = x + 30
        if x >= w:
            y = y + 30
            x = 0
        if y >= h:
            x = y = 0
        win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_WINLOGO))
        x = x + 30
        if x >= w:
            y = y + 30
            x = 0
        if y >= h:
            x = y = 0
        win32gui.InvertRect(hdc, (0, 0, w ,h))

ask = messagebox.askyesno(title="Not a Virus", message="This is not virus, only effects, all texts are fake. You can close virus with Process Manager. Are you sure to continue?")
if ask:
    virus(x, y)
else:
    messagebox.showwarning(title="Not A Virus", message="Okay, its your choice!")
