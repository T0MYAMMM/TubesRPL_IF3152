from tkinter import * 
import tkinter
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


#------function sementara------#
def open_tambahbarang():
    leaf = Toplevel()
    new_window = tambahBarang(leaf)
    leaf.configure(background='white')
    width= 1280               
    height= 720              
    leaf.geometry("%dx%d+0+0" % (width, height))

def print_list_barang(list_barang):
    for x in list_barang:
        x.print_all_attributes()

def main_program():
    #============================KONFIGURASI============================#
    root = Tk() 
    root.configure(background='white')
    root.title("Grocery Store Search Engine")
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

    #==========================TAMPILAN PRODUK==========================#
    def get_data_barang(barang, j):
        if (j == 0):
            return barang.get_nama()
        elif (j == 1):
            return barang.get_harga()
        elif (j == 2):
            return barang.get_kuantitas()

    def get_list_barang(barang, i):
        list_barang = (
            #str(barang[i].get_nama()),
            str(barang[i].get_harga()),
            str(barang[i].get_ukuran()),
            str(barang[i].get_kuantitas()),
            str(barang[i].get_kategori()),
            "ini tanggal",
            str(barang[i].get_supplier()),
            str(barang[i].get_penyimpanan()))
        return list_barang

    def view_SearchResult(list_barang, view):
        clear_view(view_listBarang)
        #label_namaBarang = Label(frame_listBarang, width = 12, text="Nama", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
        #label_hargaBarang = Label(frame_listBarang, width = 12, text="Harga", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
        #label_kuantitasBarang = Label(frame_listBarang, width = 12, text="Kuantitas", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
        #label_storageBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")
        #label_supplierBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")

        #label_namaBarang.grid(row=0, column=0)
        #label_hargaBarang.grid(row=0, column=1)
        #label_kuantitasBarang.grid(row=0, column=2)

        for i in range(len(list_barang)):
            view.insert('', 'end', text=list_barang[i].get_nama(), values=get_list_barang(list_barang, i))
    
    def view_Barang(listBarang, view):
        for i in range(len(listBarang)):
            view.insert('', 'end', text=listBarang[i].get_nama(), values=get_list_barang(listBarang, i))
                #info = Label(frame_listBarang, text=get_data_barang(listBarang[i], j), width = 12, font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
                #info.grid(row=i+1, column=j)

    #===========================CLEAR DATA=============================# 
    def clear_frame(nama_frame):
        for widgets in nama_frame.winfo_children():
            widgets.destroy()   

    def clear_view(view):
        for item in view.get_children():
            view.delete(item)

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
    search_button = Button(frame_search, width=50, height=50, image = searchImg, bg="white", bd = 0, highlightthickness=0, command = lambda : view_SearchResult(SearchNama(Search_Bar.get()), view_listBarang))
    search_button.grid(row=1, column=4, padx=2, pady=20)
    tambahBarang_button = Button(frame_search, width=50, height=50, image = tambahBarangImg, bg="white", bd = 0, highlightthickness=0, command = lambda : open_tambahbarang())
    tambahBarang_button.grid(row=1, column=5, padx=2, pady=20)

    #=========================PRODUK KOSONG BUTTON======================#
    def searchEmptyProduct():
        view_SearchResult(SearchStokKosong(), view_listBarang)
        pass
    sEP_button = RoundedButton(frame_search, width=250, height=60, text="CARI PRODUK KOSONG", size = 15, radius=25, bg='white',btnbackground="#FBBC05", btnforeground="#fff", clicked=searchEmptyProduct)
    sEP_button.grid(row=2, column=0, columnspan=2)

    #==========================CARI KATEGORI=============================#
    def open_editbarang():
        leaf = Toplevel()
        new_window = editBarang(leaf)
        leaf.configure(background='white')
        width= 1280               
        height= 720              
        leaf.geometry("%dx%d+0+0" % (width, height))

    def search_Category(category):
        #view_SearchResult(search_Category(category), view_listBarang)
        pass
    sC_button = RoundedButton(frame_search, width=200, height=60, text="CARI KATEGORI", size = 15, radius=25, bg='white',btnbackground="#34A853", btnforeground="#fff", clicked=lambda : view_SearchResult(SearchKategori(Search_Bar.get()), view_listBarang))
    sC_button.grid(row=2, column=2, columnspan=2)


    #=========================FRAME LIST BARANG==========================#  
    #LIST BARANG
    listBarang = ViewAllData() 

    #listBarang_canvas = Canvas(frame_listBarang)
    #listBarang_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #SUBJEK
    #label_namaBarang = Label(frame_listBarang, width = 12, text="Nama", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    #label_hargaBarang = Label(frame_listBarang, width = 12, text="Harga", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    #label_kuantitasBarang = Label(frame_listBarang, width = 12, text="Kuantitas", font=("Product Sans", 18), bg="white", borderwidth=1, relief="solid")
    #label_storageBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")
    #label_supplierBarang = Label(frame_listBarang, text="Penyimpanan", font=("Product Sans", 18), bg="white")

    #label_namaBarang.grid(row=0, column=0)
    #label_hargaBarang.grid(row=0, column=1)
    #label_kuantitasBarang.grid(row=0, column=2)
    #label_storageBarang.grid(row=0, column=3, padx=10)
    #label_supplierBarang.grid(row=0, column=3, padx=10)
    #self,nama, harga, gambar, ukuran, kuantitas, kategori, tanggalkadaluarsa, supplier, penyimpanan
    
    #===============================SCROLLBAR==============================#
    scrollx = Scrollbar(root, orient=HORIZONTAL)
    scrolly = Scrollbar(root, orient=VERTICAL)
    scrollx.place(relx=.25, rely=.892, width=700, height=22)
    scrolly.place(relx=.715, rely=.4, width=22, height=400)

    view_listBarang = ttk.Treeview(root)
    view_listBarang.place(relx=.25, rely=.4, width=700, height=400)
    view_listBarang.configure(
        columns=(
            "Nama",
            "Harga",
            "Kuantitas",
            "Ukuran",
            "Kategori",
            "Tgl Kadaluarsa",
            "Supplier",
            "Penyimpanan"
        )
    )
    view_listBarang.configure(selectmode="extended")
    view_listBarang.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrollx.configure(command=view_listBarang.xview)
    scrolly.configure(command=view_listBarang.yview)

    view_listBarang.tag_configure("font-style", font="Product_Sans")
    view_listBarang.tag_bind("font-style")

    view_listBarang.heading("#0", text="Nama", anchor=CENTER)
    view_listBarang.heading("#1", text="Harga", anchor=CENTER)
    view_listBarang.heading("#2", text="Kuantitas", anchor=CENTER)
    view_listBarang.heading("#3", text="Ukuran", anchor=CENTER)
    view_listBarang.heading("#4", text="Kategori", anchor=CENTER)
    view_listBarang.heading("#5", text="Kadaluarsa", anchor=CENTER)
    view_listBarang.heading("#6", text="Supplier", anchor=CENTER)
    view_listBarang.heading("#7", text="Penyimpanan", anchor=CENTER)
    

    view_listBarang.column("#0", stretch=NO, minwidth=100, width=300, anchor=W)
    view_listBarang.column("#1", stretch=NO, minwidth=40, width=150, anchor=CENTER)
    view_listBarang.column("#2", stretch=NO, minwidth=25, width=150, anchor=CENTER)
    view_listBarang.column("#3", stretch=NO, minwidth=25, width=150, anchor=CENTER)
    view_listBarang.column("#4", stretch=NO, minwidth=100, width=200, anchor=CENTER)
    view_listBarang.column("#5", stretch=NO, minwidth=50, width=150, anchor=CENTER)
    view_listBarang.column("#6", stretch=NO, minwidth=100, width=200, anchor=CENTER)
    view_listBarang.column("#7", stretch=YES, minwidth=100, width=200, anchor=CENTER)
    
    def handle_click(event):
        if view_listBarang.identify_region(event.x, event.y) == "separator":
            return "break"
    view_listBarang.bind('<Button-1>', handle_click)    


    #v_s = ttk.Scrollbar(frame_listBarang, orient=VERTICAL, command=frame_listBarang.yview)
    #v_s.pack(side=RIGHT, fill=Y)

    #frame_listBarang.configure(yscrollcommand=v_s.set)
    #frame_listBarang.bind('<Configure>', lambda e: frame_listBarang.configure(scrollregion=v_s.bbox("all")))

    #h_s = Scrollbar(root, orient='horizontal')
    #h_s.pack(side=BOTTOM, fill=X)

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
    exit_button.place(anchor = CENTER, relx = .1, rely =.1)

    #ENTITY
    view_Barang(listBarang, view_listBarang)
    #root.withdraw()
    #login(root)
    root.mainloop() #Starts the event loop for the main window


if __name__ == '__main__':
    main_program()
