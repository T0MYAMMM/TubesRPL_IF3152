from tkinter import * 
import sys 


def login(root):
    log  = Toplevel()
    input = Entry(log, width=25) 
    input.insert(0, "Password")


    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    log.geometry("%dx%d+0+0" % (width, height))

    login_button = Button(log, text="Login", command=lambda:validate())
    cancel_button = Button(log, text="Cancel", command=lambda:exit()) 
    def validate():
        if input.get() == "123": #PASSWORD
            root.deiconify() #Unhides the root window
            #print(input.get())
            log.destroy() #Removes the login window
        else:
            output = Label(log, text="Incorrect Password.")
            output.pack()
            output.place(x=708,y=420)

    def exit():
        log.destroy() #Removes the login window
        root.destroy() #Removes the hidden root window
        sys.exit() #Ends the script   
    
    input.pack() 
    login_button.pack()
    cancel_button.pack()

    input.place(x=680, y=330)
    login_button.place(x=737.5, y=355)
    cancel_button.place(x=732.5, y=385)

def showImg(root, file):
    from PIL import ImageTk,Image    
    canvas = Canvas(root, width = 600, height = 600)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open(file))  
    canvas.create_image(20, 20, anchor=NW, image=img)
