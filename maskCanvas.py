import os
import cv2
import glob
import pyautogui
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from colorama import Fore, Style

tk = Tk()
os.chdir("testImages")
inImg = "1.jpg"

tk.title("Mask Canvas")
c=Canvas(tk, width=1024, height=1024, bg='black')
c.pack(expand=NO)

bg = ImageTk.PhotoImage(Image.open(inImg))
bg_img = c.create_image(0, 0, anchor=NW, image=bg)

def fig(event):
    x1,y1=(event.x-15),(event.y-15)
    x2,y2=(event.x+15),(event.y+15)
    c.create_oval(x1, y1, x2, y2, fill='white', outline='white', tags='overlay')

def del_con(event):
    tk.title("Mask Canvas")
    plt.close('all')
    c.delete('overlay')

def img_con(event):
    c.delete(bg_img)
    c.update()
    outImg = '_Mask.'.join(inImg.split('.'))
    fileInfo = outImg.split('.')
    print("---->", outImg)
    c.postscript(file = fileInfo[0]+'.ps', colormode = 'gray')
    img  = Image.open(fileInfo[0]+'.ps').convert('L')
    img_ar = np.array(img)
    print('----------------->',img_ar.shape)
    plt.imshow(img_ar, cmap='gray')
    plt.show(block=False)
    img.save(outImg, fileInfo[1].upper())

c.bind('<B1-Motion>', fig)
c.bind('<Button-3>', del_con)
c.bind('<Button-2>', img_con)

tk.mainloop()