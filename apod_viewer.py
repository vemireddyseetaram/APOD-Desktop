from tkinter import *
from tkinter import ttk  # Import Toplevel from tkinter directly
from tkcalendar import Calendar
import os
from image_lib import download_image, save_image_file, set_desktop_background_image
from apod_api import get_apod_info

# Set the directory where the images are stored 

script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, "images")


# Function to simulate getting cached APOD dates (replace with actual implementation if available)
def get_cached_apod_dates():
    return ["2023-01-01", "2023-01-02", "2023-01-03"]  # Example date


def main():
    pass


# Function to handle the listbox selection
def listbox_select(event):
    pass  # Placeholder function, you can add functionality hereSNCLASN


# Function to show the APOD image
def show_image():
    main()  # Placeholder function, replace with actual implementation if needed


# Create the main window
root = Tk()
root.geometry("1200x800")
root.title("Astronomy Picture of the Day Viewer")


def set_Desktop_Image():
    """Set the desktop background image to the official artwork for the currently selected Pokémon."""
    selectedValue = combobox.get()
    poke_info = get_apod_info(selectedValue)
    image_data = download_image(poke_info["sprites"]["other"]["home"]["front_default"])
    image_path = os.path.join(script_dir, f"{poke_info['id']}.jpg")

    save_image_file(image_data, image_path)
    # Set the desktop background image
    set_desktop_background_image(image_path)


# Set the icon for the GUI window
root.iconbitmap(os.path.join(script_dir, "NASA_logo.ico"))
# Frame for the input widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Show button
download_button = Button(frame, text="Download", command=show_image)
download_button.grid(row=3, column=4, padx=0, pady=320)


# Calendar widget
calendar = Calendar(root, selectmode="day", year=2022, month=1, day=1)


# Function to display the calendar
def open_calendar():
    calendar.place(x=400, y=400)


# Function to update the selected date
def update_selected_date():
    selected_date.set(calendar.get_date())
    calendar.place_forget()


# Bind the calendar selection to update the selected date
calendar.bind("<<CalendarSelected>>", lambda event: update_selected_date())

# Create a frame for the "View Cached Image" section
cached_image_frame = Frame(root, bd=2, relief="groove")
cached_image_frame.place(x=10, y=400)


# Labels and dropdown for "View Cached Image"
cached_image_label = Label(cached_image_frame, text="View Cached Image")
cached_image_label.grid(row=0, column=0, padx=10, pady=10)

select_image_label = Label(cached_image_frame, text="Select Image:")
select_image_label.grid(row=1, column=0, padx=10, pady=10)

image_dropdown = ttk.Combobox(
    cached_image_frame,
    values=[
        "Select an Image",
    ],
)
image_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Create a frame for the "Get More Images" section
get_image_frame = Frame(root, bd=2, relief="groove")
get_image_frame.place(x=500, y=400)

#
# get_image_label = Label(get_image_frame, text="Get More Images")
# get_image_label.grid(row=1, column=0, padx=130, pady=50)

# Dropdown for selected date display
selected_date = StringVar()
selected_date.set("Select date:")
date_label = Label(frame, textvariable=selected_date)
date_label.grid(row=0, column=0, padx=400, pady=400)


# Label to display selected date
selected_date_label = Label(frame, text="Selected Date:")
selected_date_label.grid(row=0, column=1, padx=10, pady=10)

# Select Date Button
select_date_button = Button(frame, text="Select Date", command=open_calendar)
select_date_button.grid(row=0, column=2, padx=10, pady=10)


# Button for "Set as Desktop"
set_as_desktop_button = Button(cached_image_frame, text="Set as Desktop")
set_as_desktop_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
