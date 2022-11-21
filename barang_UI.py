from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
import PIL
from PIL import ImageTk
from PIL import Image

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
        productName = Label(productNameFrame, width=35, font=('arial', 20, 'bold'), text='Pepsodent', bg='powder blue')
        productName.pack(padx=20, pady=20, fill=BOTH)

        #Product Image
        productImageFrame = Frame(LeftFrame, bg='powder blue', relief=RIDGE)
        productImageFrame.grid(row=1, column=0)
        photo = Image.open("pepsodent.png")
        resize_image = photo.resize((150,150), Image.ANTIALIAS)
        convertedimage = ImageTk.PhotoImage(resize_image)
        productPhoto = Label(productImageFrame, image = convertedimage, width = 150, height = 150)
        productPhoto.pack(padx=1, pady=1, fill=BOTH)

        #======================Information======================

        #Product Price
        productPriceFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productPriceFrame.grid(row=2, column=0)
        productPriceLabel = Label(productPriceFrame, font=('arial', 15), text='Harga:', bg='powder blue')
        productPriceLabel.grid(row=0, column=0)
        productPrice = Label(productPriceFrame, font=('arial', 15), text='30.000', bg='powder blue')
        productPrice.grid(row=0, column=1)

        #Product Size
        productSizeFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productSizeFrame.grid(row=3, column=0)
        productSizeLabel = Label(productSizeFrame, font=('arial', 15), text='Ukuran:', bg='powder blue')
        productSizeLabel.grid(row=0, column=0)
        productSize = Label(productSizeFrame, font=('arial', 15), text='30 ml', bg='powder blue')
        productSize.grid(row=0, column=1)
        
        #Product Category
        productCategoryFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productCategoryFrame.grid(row=4, column=0)
        productCategoryLabel = Label(productCategoryFrame, font=('arial', 15), text='Kategori:', bg='powder blue')
        productCategoryLabel.grid(row=0, column=0)
        productCategory = Label(productCategoryFrame, font=('arial', 15), text='Sabun', bg='powder blue')
        productCategory.grid(row=0, column=1)

        #Product ExpDate
        productExpDateFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productExpDateFrame.grid(row=5, column=0)
        productExpDateLabel = Label(productExpDateFrame, font=('arial', 15), text='Kedaluarsa:', bg='powder blue')
        productExpDateLabel.grid(row=0, column=0)
        productExpDate = Label(productExpDateFrame, font=('arial', 15), text='15 Desember 2030', bg='powder blue')
        productExpDate.grid(row=0, column=1)

        #Product Supplier
        productSupplierFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productSupplierFrame.grid(row=6, column=0)
        productSupplierLabel = Label(productSupplierFrame, font=('arial', 15), text='Supplier:', bg='powder blue')
        productSupplierLabel.grid(row=0, column=0)
        productSupplier = Label(productSupplierFrame, font=('arial', 15), text='Haji William Gautama', bg='powder blue')
        productSupplier.grid(row=0, column=1)

        #Product Place
        productPlaceFrame = Frame(LeftFrame, height=500, bg='powder blue')
        productPlaceFrame.grid(row=7, column=0)
        productPlaceLabel = Label(productPlaceFrame, font=('arial', 15), text='Penyimpanan:', bg='powder blue')
        productPlaceLabel.grid(row=0, column=0)
        productPlace = Label(productPlaceFrame, font=('arial', 15), text='Rak nomor 3', bg='powder blue')
        productPlace.grid(row=0, column=1)

        #======================RIGHT FRAME======================

        #Rigt Frame
        RightFrame = Frame(MainFrame, bd=10, width=420, height=610, bg='powder blue', relief=RIDGE)
        RightFrame.pack(side='right', expand=True, fill=BOTH)

        #Edit Information button
        editInformationFrame = Frame(RightFrame, bg='powder blue')
        editInformationFrame.grid(row=0, column=0)
        editInformationButton = Button(editInformationFrame, font=('arial', 18, 'bold'), text='Edit Informasi', bg='magenta')
        editInformationButton.pack(side='top', padx=20, pady=20, fill=BOTH)

        #Edit Kuantity
        editKuantityFrame = Frame(RightFrame, bg='powder blue')
        editKuantityFrame.grid(row=1, column=0)
        editPlusButton = Button(editKuantityFrame, padx=10, pady=10, font=('arial', 16, 'bold'), text='+', bg='magenta')
        editPlusButton.pack(side='left', padx=20, pady=20, fill=BOTH)
        kuantityInformation = Label(editKuantityFrame, width=17, font=('arial', 23, 'bold'), text='20', bg='powder blue')
        kuantityInformation.pack(side='left', padx=20, pady=20, fill=BOTH)
        editMinusButton = Button(editKuantityFrame, padx=10, pady=10, font=('arial', 18, 'bold'), text='-', bg='magenta')
        editMinusButton.pack(side='right', padx=20, pady=20, fill=BOTH)

if __name__ == "__main__":
    root = Tk()
    application = barang(root)
    root.mainloop()
