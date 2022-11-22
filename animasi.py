import tkinter
from tkinter import *
from tkinter import messagebox
from tkvideo import tkvideo

fn = 'C:/Users/Thomas Stefen M/Dropbox/My PC (LAPTOP-VVOKBOQQ)/Documents/Python Scripts/TUBESRPL_IF3152'

window = Tk()
#window.title("Login form")
#window.geometry('800x600')
#window.configure(bg='white')

lblVideo = Label(window)
lblVideo.pack()
player = tkvideo("/Animated_logo_gsse.mp4", lblVideo, loop=1, size=(4320,1080))
player.play()
window.mainloop()