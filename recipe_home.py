import tkinter as tk
from tkinter import ttk

def open_enter_recipe():
    new_window = tk.Toplevel(root)
    new_window.title("Enter Your Recipe")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="You have selected: Enter Your Recipe")
    label.pack()

def open_search_recipe():
    new_window = tk.Toplevel(root)
    new_window.title("Search for Recipe")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="You have selected: Search for Recipe")
    label.pack()

root = tk.Tk()
root.title("Recipes")

heading_label = tk.Label(root, text="WORLD OF RECIPES", font=("Arial", 20))
heading_label.pack(pady=10)

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Enter Your Recipe")
notebook.add(frame2, text="Search for Recipe")

notebook.pack(pady=10)

option1_label = tk.Label(frame1, text="Welcome to Enter Your Recipe")
option1_label.pack(pady=20)
option1_button = tk.Button(frame1, text="Select Enter Your Recipe", command=open_enter_recipe)
option1_button.pack()

option2_label = tk.Label(frame2, text="Welcome to Search for Recipe")
option2_label.pack(pady=20)
option2_button = tk.Button(frame2, text="Select Search for Recipe", command=open_search_recipe)
option2_button.pack()

root.mainloop()