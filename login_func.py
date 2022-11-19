from tkinter import *
from functools import partial

def login(app,password_key):
    def validateLogin(password):
        print("password entered :", password.get())
        return

    #password label and password entry box
    passwordLabel = Label(app,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(app, textvariable=password, show='*').grid(row=1, column=1)  

    validateLogin = partial(validateLogin, password)

    #login button
    loginButton = Button(app, text="Login", command=validateLogin).grid(row=4, column=0)  
    
    password_key = password.get()
    return password_key

if __name__ == "__main__":
    login()