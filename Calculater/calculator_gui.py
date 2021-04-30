# Imports
import tkinter as tk

Root = tk.Tk()
Root.title()

# Make the items
text_box = tk.Entry(master=Root,columnspam = 2)

# Put the items
text_box.grid(0,0)

tk.mainloop()