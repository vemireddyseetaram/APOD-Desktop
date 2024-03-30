from tkinter import *
import apod_desktop

# Initialize the image cache
apod_desktop.init_apod_cache()

# TODO: Create the GUI
root = Tk()
root.geometry('600x400')
root.title('APOD Viewer')
def show_image(event):
    apod_desktop.main()
    button1 = Button(root, text="Show Image", command=show_image)
    button1.pack(pady=10)
    root.mainloop()
button1 = Button(root, text="Show Image", command=show_image)
button2 = Button(root, text="Quick Exit", command=root.quit)
button1.pack()
button2.pack(side=RIGHT)
                 # Add a space between buttons  
button1.pack(pady=10)
button2.pack(pady=10)
root.mainloop()




root.mainloop()