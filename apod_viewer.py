from tkinter import *
from tkinter import ttk  # Import Toplevel from tkinter directly
from tkcalendar import Calendar


# Function to simulate getting cached APOD dates (replace with actual implementation if available)
def get_cached_apod_dates():
    return ["2023-01-01", "2023-01-02", "2023-01-03"]  # Example dates


# Placeholder function for add_apod_to_cache and main functions
def add_apod_to_cache(date):
    pass


def main():
    pass


# Function to handle the listbox selection
def listbox_select(event):
    pass  # Placeholder function, you can add functionality here


# Function to show the APOD image
def show_image():
    main()  # Placeholder function, replace with actual implementation if needed


# Create the main window
root = Tk()
root.geometry("900x600")
root.title("Astronomy Picture of the Day Viewer")

# Frame for the input widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Show button
download_button = Button(frame, text="Download", command=show_image)
download_button.grid(row=3, column=4, padx=0, pady=320)


# Dropdown for selected date display
selected_date = StringVar()
selected_date.set("Select date:")
date_label = Label(frame, textvariable=selected_date)
date_label.grid(row=3, column=3, padx=450, pady=350)

# Calendar widget
calendar = Calendar(root, selectmode="day", year=2022, month=1, day=1)


# Function to display the calendar
def open_calendar():
    top = Toplevel(root)  # Use Toplevel directly from tkinter

    cal = Calendar(top, selectmode="day")
    cal.pack(pady=20)

    def on_close():
        print(cal.get_date())
        top.destroy()

    button = ttk.Button(top, text="Select", command=on_close)
    button.pack(pady=20)

# Bind the calendar to the dropdown
date_label.bind("<1>", lambda event: open_calendar())


# Function to update the selected date
def update_selected_date():
    selected_date.set(calendar.get_date())
    calendar.place_forget()


# Bind the calendar selection to update the selected date
calendar.bind("<<CalendarSelected>>", lambda event: update_selected_date())

# Create a frame for the "View Cached Image" section
cached_image_frame = Frame(root, bd=2, relief="groove")
cached_image_frame.place(x=10, y=400)  # Adjusted y-coordinate

# Labels and dropdown for "View Cached Image"
cached_image_label = Label(cached_image_frame, text="View Cached Image")
cached_image_label.grid(row=0, column=0, padx=10, pady=10)

select_image_label = Label(cached_image_frame, text="Select Image:")
select_image_label.grid(row=1, column=0, padx=10, pady=10)

image_dropdown = ttk.Combobox(
    cached_image_frame, values=["Image 1", "Image 2", "Image 3"]
)
image_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Button for "Set as Desktop"
set_as_desktop_button = Button(cached_image_frame, text="Set as Desktop")
set_as_desktop_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()



