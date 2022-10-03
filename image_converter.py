import tkinter as tk
import tkinter.filedialog as fd
import os
from PIL import Image
from pathlib import Path

window = tk.Tk()
window.title('Image converter')
window.geometry("740x520")

class ImageConverter:
    def __init__(self, main) -> None:
        # Left frame - input
        # Set up frame
        self.frame_left = tk.Frame(main, relief=tk.GROOVE, bd=1, width=40)
        self.frame_left.grid(row=0, column=0)
        # Set up buttons
        self.button_browse_images = tk.Button(self.frame_left, text='Choose images to convert', command=self.browse_images, width=40)
        self.button_browse_images.grid(row=0, column=0)
        # Set up listbox
        self.listbox_left = tk.Listbox(self.frame_left, width=40, height=30, selectmode=tk.EXTENDED)
        self.listbox_left.grid(row=1, column=0)
        # self.scroll_left = tk.Scrollbar(command=self.listbox_left.yview, orient=tk.VERTICAL)
        # self.scroll_left.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W)
        # self.listbox_left.configure(yscrollcommand=self.scroll_left.set)

        # Middle frame - settings
        # Set up frame
        self.frame_middle = tk.Frame(main, relief=tk.GROOVE, bd=1, width=80)
        self.frame_middle.grid(row=0, column=1)
        # Set up buttons
        # self.my_button1 = tk.Button(self.frame_middle, text='Print images list', command=self.clicker)
        # self.my_button1.grid(row=0, column=0)

        # self.my_button2 = tk.Button(self.frame_middle, text='Print selected images', command=self.printer)
        # self.my_button2.grid(row=1, column=0)

        self.button_remove_selected = tk.Button(self.frame_middle, text='Remove selected', command=lambda: self.remove_selected(self.listbox_left))
        self.button_remove_selected.grid(row=2, column=0, columnspan=2)

        self.button_save_all = tk.Button(self.frame_middle, text='Save all', command=self.save_all)
        self.button_save_all.grid(row=4, column=0, columnspan=2)
        # Set up drop down menu
        self.extensions = ['as is', 'JPEG', 'PNG', 'BMP']
        self.output_extension = tk.StringVar()
        self.output_extension.set(self.extensions[0])

        self.dropdown = tk.OptionMenu(self.frame_middle, self.output_extension, *self.extensions)
        self.dropdown.grid(row=3, column=1)

        self.dropdown_label = tk.Label(self.frame_middle, text='output extension:')
        self.dropdown_label.grid(row=3, column=0)


        # Right frame - output
        # Set up frame
        self.frame_right = tk.Frame(main, relief=tk.GROOVE, bd=1, width=40)
        self.frame_right.grid(row=0, column=2)
        # Set up entry
        self.label_output_directory = tk.Label(self.frame_right, text='Output directory:')
        self.label_output_directory.grid(row=0, column=0)
        self.entry_output_directory = tk.Entry(self.frame_right)
        self.entry_output_directory.grid(row=0, column=1)
        # Set up buttons
        self.button_output_directory = tk.Button(self.frame_right, text='Browse', command= self.select_directory)
        self.button_output_directory.grid(row=0, column=2)
        # Set up listbox
        self.listbox_right = tk.Listbox(self.frame_right, width=40, height=30, selectmode=tk.EXTENDED)
        self.listbox_right.grid(row=1, column=0, columnspan=3)
        # self.scroll_right = tk.Scrollbar(command=self.listbox_right.yview, orient=tk.VERTICAL)
        # self.scroll_right.grid(row=0, column=1, sticky=tk.N+tk.S+tk.W)
        # self.listbox_right.configure(yscrollcommand=self.scroll_right.set)

        # Other variables
        self.input_files = []
        self.selected = []
    
    def clicker(self):
        print(self.input_files)

    def printer(self):
        self.get_selected(self.listbox_left)
        print(self.selected)

    def browse_images(self):
        root = tk.Tk()
        root.withdraw()
        self._selected_paths = fd.askopenfilenames(parent=root,title='Select images', filetypes=[('Images', '.jpg .jpeg .jpe .png .bmp .tif .tiff')])
        root.destroy()
        self.input_files = [(path, os.path.basename(path)) for path in self._selected_paths]
        self.populate_listbox(self.input_files, self.listbox_left)
    
    def populate_listbox(self, files, lstbox):
        for file in files:
            lstbox.insert(tk.END, file[1])

    def get_selected(self, lstbox):
        selected = lstbox.curselection()
        self.selected = [self.input_files[int(x)] for x in selected]

    def remove_selected(self, lstbox):
        selected = lstbox.curselection()
        self.get_selected(lstbox)

        for i in selected[::-1]:
            lstbox.delete(i)
        for file in self.selected:
            self.input_files.remove(file)
    
    def select_directory(self):
        root = tk.Tk()
        root.withdraw()
        output_directory = fd.askdirectory()
        self.entry_output_directory.delete(0, tk.END)
        self.entry_output_directory.insert(0, output_directory)
        root.destroy()
    
    def save_all(self):
        for file in self.input_files:
            img = Image.open(file[0])
            output_filename = Path(file[0]).stem + '.jpg'
            output_directory = self.entry_output_directory.get()
            full_dir = os.path.join(output_directory, output_filename)
            print(full_dir)
            img.save(full_dir)




app = ImageConverter(window)

window.mainloop()