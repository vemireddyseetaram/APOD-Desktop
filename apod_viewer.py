from tkinter import *
from tkinter import ttk
import apod_desktop

# Initialize the image cache
apod_desktop.init_apod_cache()


# Function to handle the listbox selection
def listbox_select(event):
    pass  # Placeholder function, you can add functionality here


# Function to show the APOD image
def show_image():
    apod_desktop.add_apod_to_cache(date_entry.get())
    apod_desktop.main()


# Create the main window
root = Tk()
root.geometry("600x400")
root.title("Astronomy Picture of the Day Viewer")

# Frame for the input widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)


# Entry for APOD Date
date_entry = Entry(frame, width=10)
date_entry.insert(0, "2018-03-07")  # Default to March 7th
date_entry.grid(row=0, column=1, padx=10, pady=10)

# APOD Date label
label = Label(frame, text="View Cached Image")
label.grid(row=5, column=0, padx=10, pady=10)

# Show button
show_button = Button(frame, text="Show", command=show_image)
show_button.grid(row=0, column=2, padx=10, pady=10)

# Close button
close_button = Button(root, text="Close", command=root.quit)
close_button.pack(padx=10, pady=10)

# Frame for the listbox and scrollbar
image_frame = Frame(root)
image_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Listbox for displaying APOD images
lb = Listbox(image_frame, selectmode=SINGLE, width=40)
lb.bind("<<ListboxSelect>>", listbox_select)
lb.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar for the listbox
scrollbar = Scrollbar(image_frame, orient=VERTICAL)
scrollbar.config(command=lb.yview)
scrollbar.pack(side=RIGHT, fill=Y)
lb.config(yscrollcommand=scrollbar.set)

# Frame for search and info widgets
search_info_frame = Frame(root)
search_info_frame.pack(padx=10, pady=10)

# Frame for search widgets
search_frame = LabelFrame(search_info_frame, text="Search", padx=10, pady=10)
search_frame.pack(side=LEFT, padx=10, pady=10)

# Frame for info widgets
info_frame = LabelFrame(search_info_frame, text="Info", padx=10, pady=10)
info_frame.pack(side=RIGHT, padx=10, pady=10)

# Frame for stat widgets
stat_frame = LabelFrame(root, text="Stat", padx=10, pady=10)
stat_frame.pack(padx=10, pady=10)

root.mainloop()
