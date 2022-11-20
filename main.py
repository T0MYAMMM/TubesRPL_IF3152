from tkinter import * 
from login_admin import login
import sys 
from PIL import ImageTk,Image

 
#============================KONFIGURASI============================
root = Tk() 
root.configure(background='white')
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d+0+0" % (width, height))


#DESIGN
lable_title = Label(root, text="rocery Store Search Engine", font=("Product Sans", 30, 'bold'), bg='white')
lable_title.pack()
lable_title.place(x = 525 , y = 220)

canvas_logo = Canvas(root, width = 100, height = 100, highlightthickness=0)
canvas_logo.pack()
canvas_logo.place(x = 420, y = 200)
canvas_logo.configure(background='white')

Search_Bar = Entry(root, width = 31, font=('Product Sans',20), bg='white')
Search_Bar.pack()
Search_Bar.place(x = 440, y = 340)

logo_source = Image.open("C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TubesRPL_IF3152/logo.png")
logo_source = logo_source.resize((100,100))

searchImg_source = Image.open("C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TubesRPL_IF3152/search.jpg")
searchImg_source = searchImg_source.resize((30,30))

tambahBarang_source = Image.open("C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TubesRPL_IF3152/TambahBarang_Button.png")
tambahBarang_source = tambahBarang_source.resize((30,30))

logo = ImageTk.PhotoImage(logo_source)
searchImg =ImageTk.PhotoImage(searchImg_source)
tambahBarangImg = ImageTk.PhotoImage(tambahBarang_source)

canvas_logo.create_image(1, 1, anchor = NW, image=logo)

search_button = Button(root, image = searchImg, bd = 0, highlightthickness=0)
search_button.place(x = 980, y = 345)

tambahBarang_button = Button(root, image = tambahBarangImg, bd = 0, highlightthickness=0)
tambahBarang_button.place(x = 1020, y = 345)

#login(root)
#root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window