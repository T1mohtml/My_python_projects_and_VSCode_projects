import tkinter as tk

# Function to increment the score
def click():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

# Function to reset the score
def reset():
    global score
    score = 0
    score_label.config(text=f"Score: {score}")

# Initialize the main window
root = tk.Tk()
root.title("Clicker Game")
root.geometry("400x300")

# Initialize the score
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 24))
score_label.pack(pady=20)

# Button to increment the score
click_button = tk.Button(root, text="Click me!", font=("Arial", 16), command=click)
click_button.pack(pady=20)

# Button to reset the score (extra parentheses removed)
click_button2 = tk.Button(root, text="Reset", font=("Arial", 16), command=reset)
click_button2.pack(pady=20)

# Run the main loop
root.mainloop()