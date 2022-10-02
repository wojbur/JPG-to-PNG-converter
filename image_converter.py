import tkinter as tk
import tkinter.filedialog as fd
import os

def select_files() -> tuple:
    root = tk.Tk()
    root.withdraw()
    return fd.askopenfilenames(parent=root,title='Select images', filetypes=[('Images', '.jpg .jpeg .jpe .png .bmp .tif .tiff')])

# Set up window
window = tk.Tk()
window.title('Image Converter')

# Set up buttons
frm_input = tk.Frame(window, relief=tk.GROOVE, bd=1)
btn_select_files = tk.Button(frm_input, text='Select images', command=select_files)

btn_select_files.grid(row=0, column=0)

frm_input.grid(row=0, column=0)

window.mainloop()
