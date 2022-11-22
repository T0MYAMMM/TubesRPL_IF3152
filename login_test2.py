import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from roundedbutton import *

#===============================PATH==================================#
fn = 'C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TUBESRPL_IF3152'

#===============================Configure==================================#


window = tkinter.Tk()
window.title("Login form")
window.geometry('800x600')
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

#logo_source = ImageTk.PhotoImage(Image.open(fn+"/logo_gsse.png").resize(100,100))


password_entry = tkinter.Entry(frame, show="*", font=("Product Sans", 16))
login_button = RoundedButton(frame, width=200, height=60, text="LOGIN", radius=25, bg='white', btnbackground="#4285F4", btnforeground="#fff", clicked=func)
exit_button = RoundedButton(frame, width=200, height=60, text="EXIT", radius=25, bg='white',btnbackground="#EA4335", btnforeground="#fff", clicked=func)

label_title = Label(frame, text='rocery ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#4285F4')
label_title2 = Label(frame, text='Store ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#FBBC05')
label_title3 = Label(frame, text='Search ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#34A853')
label_title4 = Label(frame, text='Engine', font=("Product Sans", 30, 'bold'), bg='white', foreground='#EA4335')


label_title.grid(row=0, column=1, pady=40)
label_title2.grid(row=0, column=2, pady=40)
label_title3.grid(row=0, column=3, pady=40)
label_title4.grid(row=0, column=4, pady=40)


canvas_logo = Canvas(frame, width = 71, height = 71, highlightthickness=0)
canvas_logo.grid(row=0, column=0, pady=40)
canvas_logo.configure(background='white')
logo_source = Image.open(fn+"/logo.png")
logo_source = logo_source.resize((70,70))
logo = ImageTk.PhotoImage(logo_source)
canvas_logo.create_image(1, 1, anchor = NW, image=logo)

password_entry.grid(row=2, column=2, columnspan=2, pady=20)
login_button.grid(row=3, column=2, columnspan=2, pady=10)
exit_button.grid(row=4, column=2, columnspan=2, pady=10)

frame.pack()

window.mainloop()