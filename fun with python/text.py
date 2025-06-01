import tkinter as tk

def on_click(event):
 print("Button clicked")


root = tk.Tk()
root.geometry("400x300")


label = tk.Label(root, text="Hello World!", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Button-1>", on_click)

root.mainloop()