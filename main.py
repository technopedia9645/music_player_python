import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from playsound import playsound
root = Tk()
btn1 = Button(root, text ="exit", command = root.destroy)
btn1.pack(pady = 10)
def music():
          file = askopenfilename(defaultextension=".mp3",filetypes=[("All Files","*.*"), ("sound files","*.mp3")])
          playsound(file)
btn2 = Button(root, text ="Open", command = music)
btn2.pack(pady = 10)
mainloop()
