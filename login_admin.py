from tkinter import * 
import sys 


def login(root):
    log  = Toplevel()
    input = Entry(log) 

    login_button = Button(log, text="Login", command=lambda:validate())
    cancel_button = Button(log, text="Cancel", command=lambda:exit()) 
    def validate():
        if input.get() == "123": #PASSWORD
            root.deiconify() #Unhides the root window
            #print(input.get())
            log.destroy() #Removes the login window

    def exit():
        log.destroy() #Removes the login window
        root.destroy() #Removes the hidden root window
        sys.exit() #Ends the script   
    input.pack() 
    login_button.pack()
    cancel_button.pack()


def showImg(root, file):
    from PIL import ImageTk,Image    
    canvas = Canvas(root, width = 600, height = 600)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open(file))  
    canvas.create_image(20, 20, anchor=NW, image=img)
