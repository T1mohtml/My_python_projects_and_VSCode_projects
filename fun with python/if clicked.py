import tkinter as tk
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("best-vines-u-stoopid.mp3")


def on_click(event):
    sound.play()  # Програвання звуку при кліку


root = tk.Tk()
root.geometry("400x300")
root.bind("<Button-1>", on_click)

root.mainloop()