from tkinter import * 
import tkinter
from tkinter import messagebox
import sys 

fn = 'C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TUBESRPL_IF3152'

def login(root):
    #===========================COLORPALETTE============================#
    #EA4335 RED
    #FBBC05 YELLOW
    #34A853 GREEN
    #4285F4 BLUE

    window = Tk()
    window.title("Login form")               
    window.geometry("%dx%d+0+0" % (800, 600))
    window.configure(bg='white')


    def login():
        password = "123"
        if password_entry.get()==password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    def exit():
            window.destroy()   

    frame = tkinter.Frame(bg='white')

    # Creating widgets
    password_entry = tkinter.Entry(frame, show="*", font=("Product Sans", 16))
    login_button = tkinter.Button(
        frame, text="LOGIN", bg="#4285F4", fg="#FFFFFF", font=("Product Sans", 16), command=login)
    exit_button = tkinter.Button(
        frame, text="EXIT", bg="#EA4335", fg="#FFFFFF", font=("Product Sans", 16), command=exit)

    # Placing widgets on the screen
    #login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    password_entry.grid(row=2, column=0, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    exit_button.grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()

def showImg(root, file):
    from PIL import ImageTk,Image    
    canvas = Canvas(root, width = 600, height = 600)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open(file))  
    canvas.create_image(20, 20, anchor=NW, image=img)

root = Tk()
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d+0+0" % (width, height))
login(root)
root.withdraw()
root.mainloop()