from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
#from pillow import image, imageTk

class tambahBarang:
    def __init__(self,root):
        self.root = root
        self.root.title("Grocery Store Search Engine")
        self.root.geometry("1280x850+0+0")
        self.root.resizable(False,False)
        self.root.configure(background='powder blue')

        #Frame Halaman Barang
        MainFrame = Frame(self.root, bd=20, width=1280, height=650, bg='cadet blue', relief=RIDGE)
        MainFrame.pack(fill=BOTH)

        #Left Frame
        LeftFrame = Frame(MainFrame, bd=10, width=620, height=650, bg='powder blue', relief=RIDGE)
        LeftFrame.pack(side='left', expand=True, fill=BOTH)

        #Tambah Barang Label
        addProductFrame = Frame(LeftFrame, height=500, bg='powder blue')
        addProductFrame.grid(row=0, column=0)
        addProduct = Label(addProductFrame, width=35, font=('arial', 20, 'bold'), text='Tambah Barang', bg='powder blue')
        addProduct.pack(padx=20, pady=20, fill=BOTH)

        #Masukkan Nama
        productName = StringVar()
        inputNameFrame = Frame(LeftFrame, height=500, bg='powder blue')
        inputNameFrame.grid(row=1, column=0)
        self.inputNameLabel = Label(inputNameFrame, font=('arial', 15), text='Masukkan nama barang:', padx=2, pady=2, bg='powder blue')
        self.inputNameLabel.grid(row=0, column=0, sticky=W)
        self.inputNameBox = ttk.Combobox(inputNameFrame, textvariable=productName, state='readonly', font=('arial', 15), width=35 )
        self.inputNameBox.grid(row=0, column=1)

        #Rigt Frame
        RightFrame = Frame(MainFrame, bd=10, width=620, height=650, bg='powder blue', relief=RIDGE)
        RightFrame.pack(side='right', expand=True, fill=BOTH)

if __name__ == "__main__":
    root = Tk()
    application = tambahBarang(root)
    root.mainloop()
