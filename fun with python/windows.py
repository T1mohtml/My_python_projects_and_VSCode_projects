import tkinter as tk
import pygame


root = tk.Tk()
root.title("Tkinter window 2560×1600")
root.geometry("2560x1600")

def on_click(event):
   print("Button clicked")



root.bind("<Button-1>", on_click)

root.mainloop()