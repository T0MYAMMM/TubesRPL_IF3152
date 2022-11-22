from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
from PIL import Image, ImageTk

from database import *

class tambahBarang:
    def __init__(self,root):
        self.root = root
        self.root.title("Grocery Store Search Engine")
        self.root.geometry("1280x850+0+0")
        self.root.configure(background='powder blue')

        #Frame Add Product
        MainFrame = Frame(self.root, bd=20, width=1280, height=650, bg='cadet blue', relief=RIDGE)
        MainFrame.pack(fill=BOTH)

        #============================LEFT============================

        #Left Frame
        LeftFrame = Frame(MainFrame, bd=10, width=500, height=650, bg='powder blue', relief=RIDGE)
        LeftFrame.pack(side='left', expand=True, fill=BOTH)

        #Add Product Label
        addProductFrame = Frame(LeftFrame, height=500, bg='powder blue')
        addProductFrame.grid(row=0, column=0)
        addProduct = Label(addProductFrame, width=20, font=('arial', 20, 'bold'), text='Tambah Barang', bg='powder blue', pady=25)
        addProduct.pack(padx=20, pady=20, fill=BOTH)

        #Variable
        productName = StringVar()
        productPrice = IntVar()
        productPicture = StringVar()  #BelumTahunCaraUploadGambar
        productSize = IntVar()
        productQuantity = IntVar()
        productCategory = StringVar()
        productExpDate = StringVar()
        productSupplier = StringVar()
        productPlace = StringVar()

        #Method


        #Input Name
        inputFrame = Frame(LeftFrame, height=500, bg='powder blue')
        inputFrame.grid(row=1, column=0)
        self.inputNameLabel = Label(inputFrame, font=('arial', 15), text='Nama barang:', padx=70, pady=0, bg='powder blue')
        self.inputNameLabel.grid(row=0, column=0, sticky=W)
        self.inputNameBox = Entry(inputFrame, textvariable=productName, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputNameBox.grid(row=0, column=1)

        #Input Price
        self.inputPriceLabel = Label(inputFrame, font=('arial', 15), text='Harga barang:', padx=70, pady=60, bg='powder blue')
        self.inputPriceLabel.grid(row=1, column=0, sticky=W)
        self.inputPriceBox = Entry(inputFrame, textvariable=productPrice, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputPriceBox.grid(row=1, column=1)

        #Input Picture
        self.inputPictureLabel = Label(inputFrame, font=('arial', 15), text='Gambar barang:', padx=70, pady=0, bg='powder blue')
        self.inputPictureLabel.grid(row=2, column=0, sticky=W)
        self.inputPictureBox = Entry(inputFrame, textvariable=productPicture, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputPictureBox.grid(row=2, column=1)

        #Input Size
        self.inputSizeLabel = Label(inputFrame, font=('arial', 15), text='Ukuran barang:', padx=70, pady=60, bg='powder blue')
        self.inputSizeLabel.grid(row=3, column=0, sticky=W)
        self.inputSizeBox = Entry(inputFrame, textvariable=productSize, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputSizeBox.grid(row=3, column=1)

        #Input Quantity
        self.inputQuantityLabel = Label(inputFrame, font=('arial', 15), text='Jumlah barang:', padx=70, pady=0, bg='powder blue')
        self.inputQuantityLabel.grid(row=4, column=0, sticky=W)
        self.inputQuantityBox = Entry(inputFrame, textvariable=productQuantity, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputQuantityBox.grid(row=4, column=1)

        #space
        spaceFrame = Frame(LeftFrame, height=70, bg='powder blue')
        spaceFrame.grid(row=2, column=0)

        #============================LEFT============================

        #Rigt Frame
        RightFrame = Frame(MainFrame, bd=10, width=620, height=650, bg='powder blue', relief=RIDGE)
        RightFrame.pack(side='right', expand=True, fill=BOTH)

        #space
        spaceFrame = Frame(RightFrame, height=125, bg='powder blue')
        spaceFrame.grid(row=0, column=0)

        #Input Category
        self.inputCategoryLabel = Label(RightFrame, font=('arial', 15), text='Kategori:', padx=70, pady=0, bg='powder blue')
        self.inputCategoryLabel.grid(row=1, column=0, sticky=W)
        self.inputCategoryBox = ttk.Combobox(RightFrame, textvariable=productCategory, state='readonly', font=('arial', 15), width=20)
        self.inputCategoryBox['value']=('sembako','obat','sabun','mainan') #ini bisa dicustom tergantung kategorinya apa aja
        self.inputCategoryBox.grid(row=1, column=1)

        #Input Exp Date
        self.inputExpDateLabel = Label(RightFrame, font=('arial', 15), text='Kadaluarsa:', padx=70, pady=60, bg='powder blue')
        self.inputExpDateLabel.grid(row=2, column=0, sticky=W)
        self.inputExpDateBox = Entry(RightFrame, textvariable=productExpDate, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputExpDateBox.grid(row=2, column=1)

        #Input Supplier
        self.inputSupplierLabel = Label(RightFrame, font=('arial', 15), text='Supplier:', padx=70, pady=0, bg='powder blue')
        self.inputSupplierLabel.grid(row=3, column=0, sticky=W)
        self.inputSupplierBox = Entry(RightFrame, textvariable=productSupplier, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputSupplierBox.grid(row=3, column=1)

        #Input Place
        self.inputPlaceLabel = Label(RightFrame, font=('arial', 15), text='Penyimpanan:  ', padx=70, pady=60, bg='powder blue')
        self.inputPlaceLabel.grid(row=4, column=0, sticky=W)
        self.inputPlaceBox = Entry(RightFrame, textvariable=productPlace, font=('arial', 15), bd=8, width=20, fg='black', justify="left")
        self.inputPlaceBox.grid(row=4, column=1)

        #Add Button
        def getList():
            list_barang = []
            list_barang.append(productName.get())
            list_barang.append(productPrice.get())
            list_barang.append(productPicture.get())
            list_barang.append(productSize.get())
            list_barang.append(productQuantity.get())
            list_barang.append(productCategory.get())
            list_barang.append(productExpDate.get())
            list_barang.append(productSupplier.get())
            list_barang.append(productPlace.get()) 
            return list_barang

        def create_barang():
            data_baru = getList()
            nama = data_baru[0]
            harga = int(data_baru[1])
            gambar = data_baru[2]
            ukuran = int(data_baru[3])
            kuantitas = int(data_baru[4])
            kategori = data_baru[5]
            tanggal = data_baru[6]
            supplier = data_baru[7]
            tempat = data_baru[8]
            
            barang_baru = Barang(nama, harga, gambar, ukuran, kuantitas, kategori, tanggal, supplier, tempat)

            return barang_baru

        """
        def Tampil():
            list = getList()
            for i in list:
                print(i)
        """

        #Add Button
        self.addButton = Button(RightFrame, padx=2, pady=2, font=('arial', 16, 'bold'), text='Tambah', bg='red', command=lambda: create_barang())
        self.addButton.grid(row=5, column=1)

if __name__ == "__main__":
    root = Tk()
    application = tambahBarang(root)
    root.mainloop()
