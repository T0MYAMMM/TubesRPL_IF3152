from tkinter import*
from tkinter import ttk
import tkinter as tk
import random
import tkinter.messagebox
from tkinter import messagebox
#from pillow import image, imageTk

from database import *

class hapusBarang:
    def __init__(self,root, barang):
        self.root = root
        self.root.title("Grocery Store Search Engine")
        self.root.geometry("650x250+0+0")
        self.root.resizable(False,False)
        self.root.configure(background='white')

        #Frame Halaman Barang
        MainFrame = Frame(self.root, width=650, height=400, bg='white')
        MainFrame.pack(expand=True,fill=BOTH)

        #Space
        spaceFrame = Frame(MainFrame, width=650, height=30, bg='white')
        spaceFrame.grid(row=1, column=0)

        #Confirmation Text
        deleteFrame = Frame(MainFrame, bg='white')
        deleteFrame.grid(row=0, column=0)
        deleteProduct = Label(deleteFrame, width=40, font=('arial', 18, 'bold'), text='Apakah anda yakin untuk menghapus produk ini?', bg='white')
        deleteProduct.pack(side='top', padx=20, pady=20, fill=BOTH)

        #Space
        spaceFrame = Frame(MainFrame, width=650, height=30, bg='white')
        spaceFrame.grid(row=1, column=0)

        #fungsi tekan
        def confirm_delete(idbarang, root):
            HapusBarang(idbarang)
            messagebox.showinfo(title="Hapus Berhasil", message="Berhasil menghapus barang dari database.")
            root.destroy()

        def cancel_delete(root):
            messagebox.showinfo(title="Hapus Gagal", message="Gagal menghapus barang dari database.")
            root.destroy()

        #Confirmation Button
        confirmationFrame = Frame(MainFrame, bg='white')
        confirmationFrame.grid(row=2, column=0)
        yesButton = Button(confirmationFrame, padx=10, pady=5, font=('arial', 16, 'bold'), text='Ya', bg='red', command = lambda : confirm_delete(barang[1], root))
        yesButton.pack(side='left', padx=20, pady=20, fill=BOTH)
        noButton = Button(confirmationFrame, padx=10, pady=5, font=('arial', 16, 'bold'), text='Tidak', bg='cyan', command = lambda: cancel_delete(root))
        noButton.pack(side='right', padx=20, pady=20, fill=BOTH)



if __name__ == "__main__":
    root = Tk()
    application = hapusBarang(root, barang)
    root.mainloop()
