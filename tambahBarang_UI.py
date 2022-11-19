from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
#from pillow import image, imageTk

class tambahBarang:
    def __init__(self,root):
        self.root = root
        self.root.title("Delete Product")
        self.root.geometry("650x300+0+0")
        self.root.configure(background='powder blue')

        #Frame Halaman Barang
        MainFrame = Frame(self.root, width=650, height=400, bg='cadet blue')
        MainFrame.pack(expand=True,fill=BOTH)

        #Confirmation Text
        deleteFrame = Frame(MainFrame, bg='powder blue')
        deleteFrame.grid(row=0, column=0)
        deleteProduct = Label(deleteFrame, width=40, font=('arial', 18, 'bold'), text='Apakah anda yakin untuk menghapus produk ini?', bg='powder blue')
        deleteProduct.pack(side='top', padx=20, pady=20, fill=BOTH)

        #Confirmation Button
        confirmationFrame = Frame(MainFrame, bg='powder blue')
        confirmationFrame.grid(row=1, column=0)
        yesButton = Button(confirmationFrame, padx=10, pady=10, font=('arial', 16, 'bold'), text='Ya', bg='powder blue')
        yesButton.pack(side='left', padx=20, pady=20, fill=BOTH)
        noButton = Button(confirmationFrame, padx=10, pady=10, font=('arial', 16, 'bold'), text='Tidak', bg='powder blue')
        noButton.pack(side='right', padx=20, pady=20, fill=BOTH)



if __name__ == "__main__":
    root = Tk()
    application = tambahBarang(root)
    root.mainloop()
