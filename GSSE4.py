from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later

root = Tk() #Declares root as the tkinter main window
top  = Toplevel() #Creates the toplevel window

entry1 = Entry(top) #Username entry
button1 = Button(top, text="Login", command=lambda:command1()) #Login button
button2 = Button(top, text="Cancel", command=lambda:command2()) #Cancel button

#ini root-nya
root.geometry('800x800')
label1 = Label(root, text="Apakah aku ganteng masseh?")

from PIL import ImageTk,Image    
canvas = Canvas(root, width = 600, height = 600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(".\sample.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img)

button3 = Button(root, text="Cium", command=lambda:command3()) #exit button




def command1():
    if entry1.get() == "123": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        print(entry1.get())
        top.destroy() #Removes the toplevel window

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script

def command3():
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script    


entry1.pack() #These pack the elements, this includes the items for the main window 
button1.pack()
button2.pack()
button3.pack()
label1.pack()

root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window