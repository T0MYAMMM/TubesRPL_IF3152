from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
#from pillow import image, imageTk

class barang:
    def __init__(self,root):
        self.root = root
        self.root.title("Grocery Store Search Engine")
        self.root.geometry("1280x850+0+0")
        self.root.configure(background='powder blue')

        #Frame Halaman Barang
        MainFrame = Frame(self.root, bd=20, width=1280, height=650, bg='cadet blue', relief=RIDGE)
        MainFrame.pack(fill=BOTH)

        #======================LEFT FRAME======================

        #Left Frame
        LeftFrame = Frame(MainFrame, bd=10, width=820, height=610, bg='powder blue', relief=RIDGE)
        LeftFrame.pack(side='left', expand=True, fill=BOTH)

        #Product Name
        productNameFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productNameFrame.grid(row=0, column=0)
        productName = Label(productNameFrame, width=40, font=('arial', 18, 'bold'), text='Barang A', bg='powder blue')
        productName.pack(padx=20, pady=20, fill=BOTH)

        #Product Image
        productImageFrame = Frame(LeftFrame, bg='powder blue', relief=RIDGE)
        productImageFrame.grid(row=1, column=0)

        #Product Information

        
        #======================RIGHT FRAME======================

        #Rigt Frame
        RightFrame = Frame(MainFrame, bd=10, width=420, height=610, bg='powder blue', relief=RIDGE)
        RightFrame.pack(side='right', expand=True, fill=BOTH)

        #Edit Information button
        editInformationFrame = Frame(RightFrame, bg='powder blue')
        editInformationFrame.grid(row=0, column=0)
        editInformationButton = Button(editInformationFrame, font=('arial', 18, 'bold'), text='Edit Informasi', bg='powder blue')
        editInformationButton.pack(side='top', padx=20, pady=20, fill=BOTH)

        #Edit Kuantity
        editKuantityFrame = Frame(RightFrame, bg='powder blue')
        editKuantityFrame.grid(row=1, column=0)
        editPlusButton = Button(editKuantityFrame, padx=10, pady=10, font=('arial', 16, 'bold'), text='+', bg='powder blue')
        editPlusButton.pack(side='left', padx=20, pady=20, fill=BOTH)
        kuantityInformation = Label(editKuantityFrame, width=17, font=('arial', 23, 'bold'), text='20', bg='powder blue')
        kuantityInformation.pack(side='left', padx=20, pady=20, fill=BOTH)
        editMinusButton = Button(editKuantityFrame, padx=10, pady=10, font=('arial', 18, 'bold'), text='-', bg='powder blue')
        editMinusButton.pack(side='right', padx=20, pady=20, fill=BOTH)

if __name__ == "__main__":
    root = Tk()
    application = barang(root)
    root.mainloop()
