

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled")

def open_file():
    # open file and dinplay its content
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    file_name = os.path.basename(file_path)
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        root.title(f"{file_name} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
    file_name = os.path.basename(file_path)
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_name} - Notepad") 


def Exit_file():
    if messagebox.askyesno("Exit", "Do you want to save changes before exiting?"):
        save_file()
        root.destroy()



# Initialize the main application window
root  = tk.Tk()
root.title("Nodepad")
root.geometry("700x550")
img = Image.open("th.jpeg")
img.save("notepad.ico", format="ICO")
root.iconbitmap("notepad.ico")


# create text area
text_area = tk.Text(root, wrap = "word", undo=True)
text_area.pack(expand = True, fill = tk.BOTH)
menu_bar = tk.Menu(root)

# creae a menu bar
menu_bar = tk.Menu(root)


# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=Exit_file)
menu_bar.add_cascade(label="file", menu=file_menu)
menu_bar.add_cascade(label="New", command = new_file)
menu_bar.add_cascade(label="Open", command=open_file)
menu_bar.add_cascade(label="Save", command=save_file)




# add the menu bar to the main waindow
root.config(menu=menu_bar)




# run the applications 
root.mainloop()