from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
from tkinter import messagebox
#from pillow import image, imageTk

from barang import *
from database import *

class editBarang:
    def __init__(self,root, barang):
        self.root = root
        self.root.title("Grocery Store Search Engine")
        self.root.geometry("700x850+0+0")
        self.root.configure(background='powder blue')

        #Frame Edit Product
        MainFrame = Frame(self.root, bd=20, width=1280, height=650, bg='cadet blue', relief=RIDGE)
        MainFrame.pack(fill=BOTH)

        #============================LEFT============================

        #Left Frame
        LeftFrame = Frame(MainFrame, bd=10, width=500, height=650, bg='powder blue', relief=RIDGE)
        LeftFrame.pack(side='left', expand=True, fill=BOTH)

        #Add Product Label
        addProductFrame = Frame(LeftFrame, height=500, bg='powder blue')
        addProductFrame.grid(row=0, column=0)
        addProduct = Label(addProductFrame, width=20, font=('arial', 20, 'bold'), text='Edit Barang', bg='powder blue', pady=25)
        addProduct.pack(padx=20, pady=20, fill=BOTH)

        #Variable
        productName = StringVar()
        productPrice = IntVar()
        productQuantity = IntVar()
        productSupplier = StringVar()
        productPlace = StringVar()

        #Input Name
        inputFrame = Frame(LeftFrame, height=500, bg='powder blue')
        inputFrame.grid(row=1, column=0)
        self.inputNameLabel = Label(inputFrame, font=('arial', 15), text='Nama barang:', padx=70, pady=0, bg='powder blue')
        self.inputNameLabel.grid(row=0, column=0, sticky=W)
        self.inputNameBox = Entry(inputFrame, textvariable=productName, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputNameBox.insert(0, barang[0])
        self.inputNameBox.grid(row=0, column=1)

        #Input Price
        self.inputPriceLabel = Label(inputFrame, font=('arial', 15), text='Harga barang:', padx=70, pady=60, bg='powder blue')
        self.inputPriceLabel.grid(row=1, column=0, sticky=W)
        self.inputPriceBox = Entry(inputFrame, textvariable=productPrice, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputPriceBox.delete(0)
        self.inputPriceBox.insert(0, barang[2])
        self.inputPriceBox.grid(row=1, column=1)

        #Input Quantity
        self.inputQuantityLabel = Label(inputFrame, font=('arial', 15), text='Jumlah barang:', padx=70, pady=0, bg='powder blue')
        self.inputQuantityLabel.grid(row=2, column=0, sticky=W)
        self.inputQuantityBox = Entry(inputFrame, textvariable=productQuantity, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputQuantityBox.delete(0)
        self.inputQuantityBox.insert(0, barang[3])
        self.inputQuantityBox.grid(row=2, column=1)

        #Input Supplier
        self.inputSupplierLabel = Label(inputFrame, font=('arial', 15), text='Supplier:', padx=70, pady=60, bg='powder blue')
        self.inputSupplierLabel.grid(row=3, column=0, sticky=W)
        self.inputSupplierBox = Entry(inputFrame, textvariable=productSupplier, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputSupplierBox.delete(0)
        self.inputSupplierBox.insert(0, barang[3])
        self.inputSupplierBox.grid(row=3, column=1)

        #Input Place
        self.inputPlaceLabel = Label(inputFrame, font=('arial', 15), text='Penyimpanan:', padx=70, pady=0, bg='powder blue')
        self.inputPlaceLabel.grid(row=4, column=0, sticky=W)
        self.inputPlaceBox = Entry(inputFrame, textvariable=productPlace, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputPlaceBox.delete(0)
        self.inputPlaceBox.insert(0, barang[3])
        self.inputPlaceBox.grid(row=4, column=1)

        #space
        spaceFrame = Frame(LeftFrame, height=70, bg='powder blue')
        spaceFrame.grid(row=2, column=0)

        #Add Button
        def getList():
            list_barang = []
            list_barang.append(productName.get())
            list_barang.append(productPrice.get())
            list_barang.append(productQuantity.get())
            list_barang.append(productSupplier.get())
            list_barang.append(productPlace.get()) 
            return list_barang

        """
        def Tampil():
            list = getList()
            for i in list:
                print(i)
        """

        def editin_dong(ID_Barang, Harga, Kuantitas, Supplier, Penyimpanan, root):
            EditInformasi(ID_Barang, Harga, Kuantitas, Supplier, Penyimpanan)
            messagebox.showinfo(title="Edit Berhasil", message="Berhasil menyimpan perubahan informasi barang ke database.")
            root.destroy()

        #Add Button
        self.addButton = Button(LeftFrame, padx=2, pady=2, font=('arial', 16, 'bold'), text='SAVE', bg='red', command=lambda: editin_dong(barang[1], productPrice.get(), productQuantity.get(), productSupplier.get(), productPlace.get(), root))
        self.addButton.grid(row=5, column=0)

        #space
        spaceFrame = Frame(LeftFrame, height=70, bg='powder blue')
        spaceFrame.grid(row=6, column=0)



if __name__ == "__main__":
    root = Tk()
    application = editBarang(root, barang)
    application.inputNameBox.insert(0, barang[0])
    application.inputPriceBox.insert(0, barang[2])
    application.inputQuantityBox.insert(0, barang[3])
    application.inputSupplierBox.insert(0, barang[7])
    application.inputPlaceBox.insert(0, barang[8])
    
    application.inputNameBox.bind("<FocusIn>", application.inputNameBox.delete(0,"end"))
    application.inputPriceBox.bind("<FocusIn>", application.inputPriceBox.delete(0,"end"))
    application.inputQuantityBox.bind("<FocusIn>", application.inputQuantityBox.delete(0,"end"))
    application.inputSupplierBox.bind("<FocusIn>", application.inputSupplierBox.delete(0,"end"))
    application.inputPlaceBox.bind("<FocusIn>", application.inputPlaceBox.delete(0,"end"))
    root.mainloop()
