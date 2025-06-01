import tkinter as tk


def on_click():
    print("Button clicked")


# Create the main window
root = tk.Tk()

# Create the button and add it to the window
button = tk.Button(root, text="click me", command=on_click)
button.pack()

# Run the application
root.mainloop()