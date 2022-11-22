from tkinter import * 
import tkinter
import ttkthemes
from tkinter import ttk
from login_test2 import login
import sys 
from PIL import ImageTk,Image
from roundedbutton import RoundedButton

#===IMPORT MODULE===#
from barang import *
from database import *
from tambahBarang_UI import tambahBarang
from editBarang_UI import editBarang

def infoBarang(root):
    window = Toplevel(background="white")
    window.geometry("1000x600")
    frame_main = Frame(window)
    frame_main.pack(side=LEFT, fill=BOTH, expand=1)

    canpas = Canvas(frame_main, background="white", highlightthickness=0)
    canpas.place(relx=0.2, rely=0.2)
    sumber = Image.open("./Login_Button.png")
    sumber = sumber.resize((200,200))
    gambar = ImageTk.PhotoImage(sumber)
    canpas.create_image(1, 1, anchor = NW, image=gambar)
   
    label = Label(frame_main, image=gambar)
root = Tk()
root.withdraw()
infoBarang(root)
root.mainloop()