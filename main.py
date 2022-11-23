from tkinter import * 
import tkinter
import ttkthemes
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
from detailBarang_UI import detailBarang
from hapusBarang_UI import hapusBarang

#------function sementara------#
def open_tambahbarang():
    leaf = Toplevel()
    new_window = tambahBarang(leaf)
    leaf.configure(background='white')
    width= 1280               
    height= 720              
    ws = leaf.winfo_screenwidth()
    hs = leaf.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    leaf.geometry("%dx%d+%d+%d" % (width, height, x, y))

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
    def get_list_barang(barang, i):
        list_barang = (
            str(barang[i].get_idbarang()),
            str(barang[i].get_harga()),
            str(barang[i].get_kuantitas()),
            str(barang[i].get_ukuran()),
            str(barang[i].get_kategori()),
            str(barang[i].get_tanggalkadaluarsa()),
            str(barang[i].get_supplier()),
            str(barang[i].get_penyimpanan()))
        return list_barang

    def view_SearchResult(list_barang, view):
        clear_view(view_listBarang)
        for i in range(len(list_barang)):
            view.insert('', 'end', text=list_barang[i].get_nama(), values=get_list_barang(list_barang, i), tags=("row"))
    
    def view_Barang(listBarang, view):
        for i in range(len(listBarang)):
            view.insert('', 'end', text=listBarang[i].get_nama(), values=get_list_barang(listBarang, i), tags=("row"))

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
    #Search_Bar.bind('<Return>', lambda : view_SearchResult(SearchNama(Search_Bar.get()), view_listBarang))

    def handler(e):
        #label= Label(win, text= "You Pressed Enter")
        #label.pack()
        view_SearchResult(SearchNama(Search_Bar.get()), view_listBarang)
    
    root.bind('<Return>', handler)

    searchImg_source = Image.open("./search.jpg")
    searchImg_source = searchImg_source.resize((30,30))
    tambahBarang_source = Image.open("./TambahBarang_Button.png")
    tambahBarang_source = tambahBarang_source.resize((40,40))

    
    searchImg =ImageTk.PhotoImage(searchImg_source)
    tambahBarangImg = ImageTk.PhotoImage(tambahBarang_source)
    search_button = Button(frame_search, width=50, height=50,image = searchImg, bg="white", bd = 0, highlightthickness=0, command = lambda : view_SearchResult(SearchNama(Search_Bar.get()), view_listBarang))
    search_button.grid(row=1, column=4, padx=2, pady=20)
    
    tambahBarang_button = Button(frame_search, width=50, height=50, image = tambahBarangImg, bg="white", bd = 0, highlightthickness=0, command = lambda : open_tambahbarang())
    tambahBarang_button.grid(row=1, column=5, padx=2, pady=20)

    #=========================PRODUK KOSONG BUTTON======================#
    def searchEmptyProduct():
        view_SearchResult(SearchStokKosong(), view_listBarang)
        pass
    sEP_button = RoundedButton(frame_search, width=220, height=50, text="CARI PRODUK KOSONG", size = 12, radius=25, bg='white',btnbackground="#FBBC05", btnforeground="#fff", clicked=searchEmptyProduct)
    sEP_button.grid(row=2, column=0, columnspan=2)

    #==========================CARI KATEGORI=============================#

    sC_button = RoundedButton(frame_search, width=200, height=50, text="CARI KATEGORI", size = 12, radius=25, bg='white',btnbackground="#34A853", btnforeground="#fff", clicked=lambda : view_SearchResult(SearchKategori(Search_Bar.get()), view_listBarang))
    sC_button.grid(row=2, column=2, columnspan=2)


    #=========================FRAME LIST BARANG==========================#  
    #LIST BARANG
    listBarang = ViewAllData() 
    
    #THREEVIEW & SCROLLBAR    
    scrollx = Scrollbar(root, orient=HORIZONTAL)
    scrolly = Scrollbar(root, orient=VERTICAL)
    scrollx.place(relx=.25, rely=.892, width=700, height=22)
    scrolly.place(relx=.715, rely=.4, width=22, height=400)

    view_listBarang = ttk.Treeview(root)
    view_listBarang.place(relx=.25, rely=.4, width=700, height=400)
    #view_listBarang.configure(style="style")
    view_listBarang.configure(
        columns=(
            "Nama",
            "ID Barang",
            "Harga",
            "Kuantitas",
            "Ukuran",
            "Kategori",
            "Tgl Kadaluarsa",
            "Supplier",
            "Penyimpanan"
        )
    )
    view_listBarang.configure(selectmode="browse")
    view_listBarang.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrollx.configure(command=view_listBarang.xview)
    scrolly.configure(command=view_listBarang.yview)

    view_listBarang.tag_configure("font-style", font="Product_Sans")
    view_listBarang.tag_bind("font-style")

    view_listBarang.heading("#0", text="Nama", anchor=CENTER)
    view_listBarang.heading("#1", text="ID", anchor=CENTER)
    view_listBarang.heading("#2", text="Harga", anchor=CENTER)
    view_listBarang.heading("#3", text="Kuantitas", anchor=CENTER)
    view_listBarang.heading("#4", text="Ukuran", anchor=CENTER)
    view_listBarang.heading("#5", text="Kategori", anchor=CENTER)
    view_listBarang.heading("#6", text="Kadaluarsa", anchor=CENTER)
    view_listBarang.heading("#7", text="Supplier", anchor=CENTER)
    view_listBarang.heading("#8", text="Penyimpanan", anchor=CENTER)
    

    view_listBarang.column("#0", stretch=NO, minwidth=100, width=300, anchor=W)
    view_listBarang.column("#1", stretch=NO, minwidth=40, width=100, anchor=CENTER)
    view_listBarang.column("#2", stretch=NO, minwidth=25, width=150, anchor=CENTER)
    view_listBarang.column("#3", stretch=NO, minwidth=25, width=150, anchor=CENTER)
    view_listBarang.column("#4", stretch=NO, minwidth=25, width=150, anchor=CENTER)
    view_listBarang.column("#5", stretch=NO, minwidth=100, width=200, anchor=CENTER)
    view_listBarang.column("#6", stretch=NO, minwidth=50, width=150, anchor=CENTER)
    view_listBarang.column("#7", stretch=NO, minwidth=100, width=200, anchor=CENTER)
    view_listBarang.column("#8", stretch=YES, minwidth=100, width=200, anchor=CENTER)
    
    style = ttkthemes.ThemedStyle(view_listBarang)
    style.theme_use('clam')
    style.configure('Threeview', font=("Product Sans", 12), cellpadding=19)
    style.configure('Threeview.Heading', font=("Product Sans", 12, "bold"))
    style.map("Threeview", background=[('selected', '#4285F4')], foreground=[('selected', '#fff')])

    def deleteBarang(barang):
        #id = view_listBarang(row_id)[0]
        leaf = Toplevel()
        new_window = hapusBarang(leaf, barang)
        leaf.configure(background='white')
        width= 650               
        height= 250
        ws = leaf.winfo_screenwidth()
        hs = leaf.winfo_screenheight()
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        leaf.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def open_infoBarang(barang):
        root.withdraw()
        detailBarang(barang, root)

    def open_editbarang(barang):
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

    def postPopUpMenu(event):
        row_id = view_listBarang.identify_row(event.y)
        view_listBarang.selection_set(row_id)
        row_values = view_listBarang.item(row_id)['values']
        #print(row_id)
        #view_listBarang.item(row_id)["text"]
        row_values.insert(0, view_listBarang.item(row_id)["text"])
        popUpMenu = tkinter.Menu(view_listBarang, tearoff=0, font=("Product Sans", 11))
        popUpMenu.add_command(label="Lihat Informasi Detail", accelerator="Ctrl+L", command=lambda:open_infoBarang(row_values))
        popUpMenu.add_command(label="Edit/Update", accelerator="Ctrl+E", command=lambda:open_editbarang(row_values))
        popUpMenu.add_command(label="Delete", accelerator="Delete", command=lambda: deleteBarang(row_values))
        popUpMenu.post(event.x_root, event.y_root)

    view_listBarang.tag_bind("row", "<Button-3>", lambda event: postPopUpMenu(event))

    def handle_click(event):
        if view_listBarang.identify_region(event.x, event.y) == "separator":
            return "break"
    view_listBarang.bind('<Button-1>', handle_click)    

    

    #=============================EXIT BUTTON=============================#
    def exit():
        root.destroy()   
        sys.exit()
    exit_button = RoundedButton(frame_search, width=150, height=50, text="EXIT", size=12, radius=25, bg='white',btnbackground="#EA4335", btnforeground="#fff", clicked=exit)
    

    #================================PELETAKAN===============================# 
    frame_label.place(anchor = CENTER, relx = .5, rely = .15)
    frame_search.place(anchor = CENTER, relx = .5, rely = .3)
    frame_listBarang.place(anchor = N, relx = .5, rely =.4)

    #sEP_button.place(relx = .6, rely =.45)
    #sC_button.place(relx = .4, rely =.45)
    exit_button.grid(row=2,column=4, columnspan=2)

    #ENTITY
    view_Barang(listBarang, view_listBarang)
    root.withdraw()
    login(root)
    root.mainloop() #Starts the event loop for the main window


if __name__ == '__main__':
    main_program()
