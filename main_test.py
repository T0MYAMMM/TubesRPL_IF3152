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


    #DESIGN
    #===========================COLORPALETTE============================#
    #EA4335 RED
    #FBBC05 YELLOW
    #34A853 GREEN
    #4285F4 BLUE

    Title = Text(root, font=("Product Sans", 30, 'bold'), bg='white', bd=0, highlightthickness=0)
    Title.insert(INSERT, "rocery Store Search Engine")
    Title.pack()
    Title.place(x = 525 , y = 220)
    Title.tag_config("blue", foreground="#4285F4")
    Title.tag_config("green", foreground="#34A853")
    Title.tag_config("yellow", foreground="#FBBC05")
    Title.tag_config("red", foreground="#EA4335")
    Title.tag_add("blue", "1.0", "1.6")
    Title.tag_add("green", "1.7", "1.12") 
    Title.tag_add("yellow", "1.13", "1.19")
    Title.tag_add("red", "1.20", "1.26")

    canvas_logo = Canvas(root, width = 101, height = 101, highlightthickness=0)
    canvas_logo.pack()
    canvas_logo.place(x = 420, y = 200)
    canvas_logo.configure(background='white')

    Search_Bar = Entry(root, width = 31, font=('Product Sans',20), bg='white')
    Search_Bar.pack()
    Search_Bar.place(x = 440, y = 340)

    logo_source = Image.open("./logo.png")
    logo_source = logo_source.resize((100,100))

    searchImg_source = Image.open("./search.jpg")
    searchImg_source = searchImg_source.resize((30,30))

    tambahBarang_source = Image.open("./TambahBarang_Button.png")
    tambahBarang_source = tambahBarang_source.resize((30,30))

    logo = ImageTk.PhotoImage(logo_source)
    searchImg =ImageTk.PhotoImage(searchImg_source)
    tambahBarangImg = ImageTk.PhotoImage(tambahBarang_source)

    canvas_logo.create_image(1, 1, anchor = NW, image=logo)

    search_button = Button(root, image = searchImg, bd = 0, highlightthickness=0)
    search_button.place(x = 980, y = 344)

    tambahBarang_button = Button(root, image = tambahBarangImg, bd = 0, highlightthickness=0)
    tambahBarang_button.place(x = 1020, y = 344)
    root.withdraw()
    login(root)
    #root.withdraw()
    root.mainloop() #Starts the event loop for the main window


if __name__ == '__main__':
    main_program()
