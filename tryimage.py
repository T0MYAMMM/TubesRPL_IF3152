# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
root = Tk()

# Set the geometry of tkinter frame
root.geometry("700x450")

# Create a canvas widget
canvas= Canvas(root, width=600, height=400)
canvas.pack()

# Load an image
img=ImageTk.PhotoImage(Image.open("sample.jpg"))

# Add image to the Canvas Items
canvas.create_image(250, 250, anchor=CENTER, image=img)

root.mainloop()