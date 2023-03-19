import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    # get the directory containing the files to be renamed
    directory = filedialog.askdirectory(title="Select Directory")
    # check if a directory was selected
    if directory:
        # set the prefix for the new file names
        prefix = prefix_entry.get()
        # set the starting number for the new file names
        start_num = int(num_entry.get())
        # get the new file extension
        new_ext = ext_entry.get()
        # loop through all the files in the directory
        for filename in os.listdir(directory):
            # check that the file is not a directory
            if os.path.isfile(os.path.join(directory, filename)):
                # get the original file extension
                old_ext = os.path.splitext(filename)[1]
                # check if the old and new extensions are the same
                if old_ext != new_ext:
                    # construct the new file name with the prefix, number, and new extension
                    new_filename = prefix + str(start_num) + new_ext
                else:
                    # construct the new file name with the prefix and number (keeping the original extension)
                    new_filename = prefix + str(start_num) + old_ext
                # rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                # increment the number for the next file
                start_num += 1
        # show a message box when the renaming is complete
        tk.messagebox.showinfo("File Renamer", "Files renamed successfully!")

# create the main window
window = tk.Tk()
window.title("Bulk File Renamer")

# set the background color of the window
window.configure(bg='#333333')

# create a label and entry for the prefix
prefix_label = tk.Label(window, text="Prefix:", bg='#333333', fg='white')
prefix_label.grid(row=0, column=0, padx=5, pady=5)
prefix_entry = tk.Entry(window, width=40)
prefix_entry.grid(row=0, column=1, padx=5, pady=5)

# create a label and entry for the starting number
num_label = tk.Label(window, text="Starting Number:", bg='#333333', fg='white')
num_label.grid(row=1, column=0, padx=5, pady=5)
num_entry = tk.Entry(window, width=40)
num_entry.grid(row=1, column=1, padx=5, pady=5)

# create a label and entry for the new extension
ext_label = tk.Label(window, text="New Extension (include the '.'): ", bg='#333333', fg='white')
ext_label.grid(row=2, column=0, padx=5, pady=5)
ext_entry = tk.Entry(window, width=10)
ext_entry.grid(row=2, column=1, padx=5, pady=5)

# create a button to initiate the renaming process
rename_button = tk.Button(window, text="Rename Files", width=40, command=rename_files)
rename_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# run the main loop
window.mainloop()
