from tkinter import * 
import tkinter
import ttkthemes
from tkinter import ttk
from login_test2 import login
import sys 
from PIL import ImageTk,Image
from roundedbutton import RoundedButton
from tkinter import messagebox
 

#===IMPORT MODULE===#
from barang import *
from database import *
from tambahBarang_UI import tambahBarang
from editBarang_UI import editBarang

#===================KONFIGURASI=================#
def detailBarang(barang, root):
    window = Toplevel()
    window.title("ini scrollbar")
    window.geometry("1000x600")

    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, background='white')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview) 
    scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas, background='white', highlightbackground='black', highlightthickness=5)
    third_frame = Frame(my_canvas, background="black", highlightbackground="red", highlightthickness=5) 

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    third_frame.place(relx=.6, rely=.5)
    canvas_gambar = Canvas(second_frame, width=400, height=400, background='blue')

    img_source = Image.open("./sample.jpg")
    img_source = img_source.resize((400,400), resample=1)
    gambar = ImageTk.PhotoImage(img_source)
    canvas_gambar.create_image(200,200, anchor = "center", image=gambar)
    canvas_gambar.pack(padx=30, pady=10)


    informasi_frame1 = Frame(second_frame, background='green')
    informasi_frame2 = Frame(second_frame, background='yellow')
    informasi_frame3 = Frame(third_frame, background='brown')
    informasi_frame1.pack(side=LEFT, padx=(30,0), pady=10)
    informasi_frame2.pack(side=TOP, fill=X, padx=(0,30), pady=10)
    informasi_frame3.pack(side=RIGHT, fill=Y)

    #=======================FRAME INFORMASI 1-2=======================#

    nama_barang = barang[0]
    gambar_barang = SearchNama(barang[0])[1]
    ID_barang = barang[1]
    harga_barang = barang[2]
    kuantitas_barang = barang[3]
    ukuran_barang = barang[4]
    kategori_barang = barang[5]
    kadaluarsa_barang = barang[6]
    supplier_barang = barang[7]
    penyimpanan_barang = barang[8]

    label_nama_title = Label(informasi_frame1, text="Nama", font=("Product Sans", 15, "bold"), width=12, foreground='#EA4335', background="#fff")
    label_harga_title = Label(informasi_frame1, text="Harga", font=("Product Sans", 15, "bold"), width=12, foreground='#EA4335', background="#fff")
    label_ukuran_title = Label(informasi_frame1, text="Ukuran", font=("Product Sans", 15, "bold"),  width=12, foreground='#EA4335', background="#fff")
    label_kategori_title = Label(informasi_frame1, text="Kategori", font=("Product Sans", 15, "bold"),  width=12, foreground='#EA4335', background="#fff")

    label_nama = Label(informasi_frame2, text=nama_barang, font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff")
    label_harga = Label(informasi_frame2, text=harga_barang, font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff")
    label_ukuran = Label(informasi_frame2, text=ukuran_barang, font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff")
    label_kategori = Label(informasi_frame2, text=kategori_barang, font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff")

    label_nama_title.pack(padx=10, pady=5)
    label_harga_title.pack(padx=10, pady=5)
    label_ukuran_title.pack(padx=10, pady=5)
    label_kategori_title.pack(padx=10, pady=5)

    label_nama.pack(padx=10, pady=5)
    label_harga.pack(padx=10, pady=5)
    label_ukuran.pack(padx=10, pady=5)
    label_kategori.pack(padx=10, pady=5)

    #=======================FRAME INFORMASI 3=======================#
    label_kuantitas = Label(informasi_frame3, text=kuantitas_barang, font=("Product Sans", 15), width=5, height=2, foreground='#EA4335', background="#fff")
    label_kuantitas.pack(padx=10,pady=10)

    def command_edit(barang):
        leaf = Toplevel()
        new_window = editBarang(leaf, barang)
        leaf.configure(background='white')
        width= 700               
        height= 850              
        ws = leaf.winfo_screenwidth()
        hs = leaf.winfo_screenheight()
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        leaf.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def command_add(label_kuantitas, barang):
        #global kuantitas_barang = kuantitas_barang
        kuantitas_barang = barang[3]+1
        EditKuantitas(barang[1], kuantitas_barang)
        label_kuantitas.config(text=kuantitas_barang)
        
    def command_subtract(label_kuantitas, barang):
        #global kuantitas_barang = kuantitas_barang
        kuantitas_barang = barang[3]-1
        EditKuantitas(barang[1], kuantitas_barang)
        label_kuantitas.config(text=kuantitas_barang)

    def command_exit(ID_Barang, Harga, Kuantitas, Supplier, Penyimpanan):
        EditInformasi(ID_Barang, Harga, Kuantitas, Supplier, Penyimpanan)
        messagebox.showinfo(title="Kembali", message="Berhasil menyimpan perubahan informasi barang ke database.")
        window.destroy()
        root.deiconify()


    edit_button = Button(informasi_frame3, text="Edit", font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff", command=lambda:command_edit(barang))
    add_button = Button(informasi_frame3, text="+", font=("Product Sans", 15, "bold"), height=1, foreground='#EA4335', background="#fff", command=lambda:command_add(label_kuantitas, barang))
    subtract_button = Button(informasi_frame3, text="-", font=("Product Sans", 15, "bold"),  height=1, foreground='#EA4335', background="#fff", command=lambda:command_subtract(label_kuantitas, barang))
    back_button = Button(informasi_frame3, text="Save", font=("Product Sans", 15), width=20, foreground='#EA4335', background="#fff", command=lambda:command_exit(barang[1], harga_barang, kuantitas_barang, barang[7], barang[8]))

    edit_button.pack(padx=10,pady=10)
    add_button.pack(padx=10,pady=10)
    subtract_button.pack(padx=10,pady=10)
    back_button.pack(padx=0, pady=10)
    add_button.place_configure(relx=.68, rely=.11)
    subtract_button.place_configure(relx=.21, rely=.11)

    window.mainloop()
