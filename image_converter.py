import tkinter as tk
import tkinter.filedialog as fd
import os

def select_files() -> tuple:
    root = tk.Tk()
    root.withdraw()
    files = fd.askopenfilenames(parent=root,title='Select images', filetypes=[('Images', '.jpg .jpeg .jpe .png .bmp .tif .tiff')])
    root.destroy()
    return files

def select_files_button():
    pass

# Set up window
window = tk.Tk()
window.geometry("700x350")
window.title('Image Converter')

C = []
# Set up buttons
frame_input = tk.Frame(window, relief=tk.GROOVE, bd=1)
button_select_files = tk.Button(frame_input, text='Select images', command= lambda: C==select_files())

button_select_files.grid(row=0, column=0)

# Set up selected files listbox
# lstbox_input = tk.Listbox(frm_input, )
print(C)

frame_input.grid(row=0, column=0)

window.mainloop()
