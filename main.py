from tkinter import * 
import tkinter
from login_test3 import login
import sys 
from PIL import ImageTk,Image
from roundedbutton import RoundedButton

def main_program():
    #============================KONFIGURASI============================#
    root = Tk() 
    root.configure(background='white')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("%dx%d+0+0" % (width, height))
    frame_search = tkinter.Frame(root, bg='white')
    frame_label = tkinter.Frame(root, bg="white")
    frame_listBarang = tkinter.Frame(root,height=100, width=100, bg="white")
    
    
    #===========================COLORPALETTE============================#
    #EA4335 RED
    #FBBC05 YELLOW
    #34A853 GREEN
    #4285F4 BLUE

    #=============================FRAME LABEL============================#
    canvas_logo = Canvas(frame_label, width = 71, height = 71, highlightthickness=0)
    canvas_logo.grid(row=0, column=0, pady=40)
    canvas_logo.configure(background='white')
    label_title = Label(frame_label, text='rocery ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#4285F4')
    label_title2 = Label(frame_label, text='Store ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#FBBC05')
    label_title3 = Label(frame_label, text='Search ', font=("Product Sans", 30, 'bold'), bg='white', foreground='#34A853')
    label_title4 = Label(frame_label, text='Engine', font=("Product Sans", 30, 'bold'), bg='white', foreground='#EA4335')
    label_title.grid(row=0, column=1, pady=40)
    label_title2.grid(row=0, column=2, pady=40)
    label_title3.grid(row=0, column=3, pady=40)
    label_title4.grid(row=0, column=4, pady=40)

    logo_source = Image.open("./logo.png")
    logo_source = logo_source.resize((70,70))
    logo = ImageTk.PhotoImage(logo_source)
    canvas_logo.create_image(1, 1, anchor = NW, image=logo)

    #==========================FRAME SEARCH BAR==========================#
    Search_Bar = Entry(frame_search, width = 30, font=('Product Sans',20), bg='white')
    Search_Bar.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

    searchImg_source = Image.open("./search.jpg")
    searchImg_source = searchImg_source.resize((30,30))
    tambahBarang_source = Image.open("./TambahBarang_Button.png")
    tambahBarang_source = tambahBarang_source.resize((40,40))

    
    searchImg =ImageTk.PhotoImage(searchImg_source)
    tambahBarangImg = ImageTk.PhotoImage(tambahBarang_source)
    search_button = Button(frame_search, image = searchImg, bd = 0, highlightthickness=0)
    search_button.grid(row=1, column=4, padx=10, pady=20)
    tambahBarang_button = Button(frame_search, image = tambahBarangImg, bd = 0, highlightthickness=0)
    tambahBarang_button.grid(row=1, column=5, padx=10, pady=20)

    #=========================PRODUK KOSONG BUTTON======================#
    def searchEmptyProduct():
        #root.destroy()   
        #sys.exit()
        pass
    sEP_button = RoundedButton(frame_search, width=250, height=60, text="CARI PRODUK KOSONG", size = 15, radius=25, bg='white',btnbackground="#FBBC05", btnforeground="#fff", clicked=searchEmptyProduct)
    sEP_button.grid(row=2, column=0, columnspan=2)

    #==========================CARI KATEGORI=============================#
    def searchCategory():
        #root.destroy()   
        #sys.exit()
        pass
    sC_button = RoundedButton(frame_search, width=200, height=60, text="CARI KATEGORI", size = 15, radius=25, bg='white',btnbackground="#34A853", btnforeground="#fff", clicked=searchCategory)
    sC_button.grid(row=2, column=2, columnspan=2)


    #=========================FRAME LIST BARANG==========================#  
    #LIST BARANG
    listBarang = [
                ["INDOMILK", 7000, "inigambar", 10, "minuman", "12/10/2022", "INDOMILK", "RAK1"], 
                ["ADEM SARI", 5000, "inigambar", 4, "minuman", "12/10/2022", "TOKOOBAT", "RAK2"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"],
                ["BIMOLY 2L", 23000, "inigambar", 25, "bahan dapur", "12/10/2022", "BIMOLY", "RAK3"]
                ]

    #SUBJEK
    label_namaBarang = Label(frame_listBarang, width = 12, text="Nama", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    label_hargaBarang = Label(frame_listBarang, width = 12, text="Harga", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    label_kuantitasBarang = Label(frame_listBarang, width = 12, text="Kuantitas", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    #label_storageBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")
    #label_supplierBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")

    label_namaBarang.grid(row=0, column=0)
    label_hargaBarang.grid(row=0, column=1)
    label_kuantitasBarang.grid(row=0, column=2)
    #label_storageBarang.grid(row=0, column=3, padx=10)
    #label_supplierBarang.grid(row=0, column=3, padx=10)
    #self,nama, harga, gambar, ukuran, kuantitas, kategori, tanggalkadaluarsa, supplier, penyimpanan

    #ENTITY
    for i in range(len(listBarang)):
        for j in range(3):
            info = Label(frame_listBarang, text=listBarang[i][j], width = 12, font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
            info.grid(row=i+1, column=j)
        
    #===============================SCROLLBAR==============================#

    v_s = Scrollbar(root)
    v_s.pack(side=RIGHT, fill=Y)

    h_s = Scrollbar(root, orient='horizontal')
    h_s.pack(side=BOTTOM, fill=X)

    #v_s.config(command=root.xview) #for horizontal scrollbar
    #h_s.config(command=root.yview) #for vertical scrollbar   

    #=============================EXIT BUTTON=============================#
    def exit():
        root.destroy()   
        sys.exit()
    exit_button = RoundedButton(root, width=200, height=60, text="EXIT", radius=25, bg='white',btnbackground="#EA4335", btnforeground="#fff", clicked=exit)
    

    #================================PELETAKAN===============================# 
    frame_label.place(anchor = CENTER, relx = .5, rely = .15)
    frame_search.place(anchor = CENTER, relx = .5, rely = .3)
    frame_listBarang.place(anchor = N, relx = .5, rely =.4)

    #sEP_button.place(relx = .6, rely =.45)
    #sC_button.place(relx = .4, rely =.45)
    exit_button.place(anchor = CENTER, relx = .1, rely =.8)

    root.withdraw()
    login(root)
    root.mainloop() #Starts the event loop for the main window


if __name__ == '__main__':
    main_program()
