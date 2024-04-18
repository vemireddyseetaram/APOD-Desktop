from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import os
from apod_api import get_apod_info
from image_lib import set_desktop_background_image, download_image, save_image_file
from apod_desktop import get_apod_info, image_cache_db


# Set the directory where the images are stored
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, "images")


# Function to simulate getting cached APOD dates (replace with actual implementation if available)
def get_cached_apod_dates():
    # Return a list of cached APOD dates 
    # Example implementation:
    cached_dates = ["2023-01-01", "2023-01-02", "2023-01-03"]  # Example date
    return cached_dates
    

    
def main():
    # Get cached APOD dates 
    cached_dates = get_cached_apod_dates()
    # Create a combobox with cached APOD dates
    combobox_dates = ttk.Combobox(root, values=cached_dates)
    combobox_dates.pack()
    # Create a button to show the APOD image 
    button = Button(root, text="Set Desktop Image", command=set_desktop_image)
    button.pack()
    

# Function to show the APOD image
def show_image():
    
    main()  # Placeholder function, replace with actual implementation if needed


# Create the main window
root = Tk()
root.geometry("1200x800")
root.title("Astronomy Picture of the Day Viewer")



    # Load and display the NASA logo image
nasa_logo_img = PhotoImage(file="NASA_logo.png")
logo_label = Label(root, image=nasa_logo_img)
logo_label.pack()


# Function to set desktop image
def set_desktop_image():
    selectedValue = combobox_dates.get()
    apod_info = get_apod_info(selectedValue)
    image_data = download_image(apod_info["url"])
    image_path = os.path.join(images_dir, f"{selectedValue}.jpg")

    save_image_file(image_data, image_path)
    # Set the desktop background image
    set_desktop_background_image(image_path)


combobox_dates = ttk.Combobox(root)


# Set the icon for the GUI window
root.iconbitmap(os.path.join(script_dir, "NASA_logo.ico"))

# Frame for the input widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

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



# Label to display selected date
selected_date = StringVar()
selected_date.set("Select date:")
date_label = Label(frame, textvariable=selected_date)
date_label.grid(row=0, column=2, padx=10, pady=10)

# Label to display selected date
selected_date_label = Label(frame, text="Selected Date:")
selected_date_label.grid(row=0, column=0, padx=10, pady=10)

# Select Date Button
select_date_button = Button(frame, text="Select Date", command=open_calendar)
select_date_button.grid(row=0, column=0, padx=400, pady=400)

# Create a frame to display APOD information
apod_info_frame = Frame(root, bd=2, relief="groove")
apod_info_frame.place(x=250, y=100)


# Function to display APOD information on the frame
def display_apod_info(apod_info):
    # Clear any previous information
    for widget in apod_info_frame.winfo_children():
        widget.destroy()

    # Display APOD information
    for key, value in apod_info.items():
        label = Label(apod_info_frame, text=f"{key.capitalize()}: {value}")
        label.pack(anchor="w")


# Function to update APOD information based on selected date
def update_apod_info():
    selected_date = calendar.get_date()
    apod_info = get_apod_info(selected_date)
    if apod_info:
        display_apod_info(apod_info)
    else:
        display_apod_info({"Error": "Failed to retrieve APOD information."})


# Bind the calendar selection to update APOD information
calendar.bind("<<CalendarSelected>>", lambda event: update_apod_info())

apod_info_frame = Frame(root, bd=2, relief="groove")
apod_info_frame.pack(padx=10, pady=10)

# Initially, display APOD information for the default selected date
update_apod_info()
# Populate the cached images dropdown menu

# Function to populate the cached images dropdown menu
def populate_cached_images_menu():
    dates = get_cached_apod_dates()
    image_dropdown["values"] = dates
    + ["Select an Image"] 
    # Set the default value to "Select an Image"
    image_dropdown.current(len(dates))
    # Function to display cached image on the frame
def display_cached_image():
        # Clear any previous information
        for widget in apod_info_frame.winfo_children():
            widget.destroy()
            selected_date = image_dropdown.get()
            if selected_date == "Select an Image":
                return
            
root.mainloop()
