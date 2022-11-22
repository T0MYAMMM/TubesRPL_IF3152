from tkinter import * 
import tkinter
from login_test3 import login
import sys 
from PIL import ImageTk,Image

def main_program():
    #============================KONFIGURASI============================#
    root = Tk() 
    root.configure(background='white')
    width= root.winfo_screenwidth()               
    height= root.winfo_screenheight()               
    root.geometry("%dx%d+0+0" % (width, height))
    frame = tkinter.Frame(root, bg='yellow')
    frame_label = tkinter.Frame(root, bg="black")
    frame_listBarang = tkinter.Frame(root,height=100, width=100, bg="blue")
    
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
    Search_Bar = Entry(frame, width = 25, font=('Product Sans',20), bg='white')
    Search_Bar.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

    searchImg_source = Image.open("./search.jpg")
    searchImg_source = searchImg_source.resize((30,30))
    tambahBarang_source = Image.open("./TambahBarang_Button.png")
    tambahBarang_source = tambahBarang_source.resize((40,40))

    
    searchImg =ImageTk.PhotoImage(searchImg_source)
    tambahBarangImg = ImageTk.PhotoImage(tambahBarang_source)
    search_button = Button(frame, image = searchImg, bd = 0, highlightthickness=0)
    search_button.grid(row=1, column=4, padx=10, pady=20)
    tambahBarang_button = Button(frame, image = tambahBarangImg, bd = 0, highlightthickness=0)
    tambahBarang_button.grid(row=1, column=5, padx=10, pady=20)

    #=========================FRAME LIST BARANG==========================#    
    label_barang1 = Label(frame_listBarang, text="Barang1", font=("Product Sans", 18))
    label_barang1.grid(row=0, column=0)
    
    #===============================SCROLLBAR==============================#



    #=========================PELETAKAN FRAME===========================# 
    frame_label.place(anchor = CENTER, relx = .5, rely = .2)
    frame.place(anchor = CENTER, relx = .5, rely = .4)
    frame_listBarang.place(anchor = CENTER, relx = .5, rely = .6)

    root.withdraw()
    login(root)
    root.mainloop() #Starts the event loop for the main window


if __name__ == '__main__':
    main_program()
