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
img = "1.jpg"

tk.title("Mask Canvas")
c=Canvas(tk, width=1024, height=1024, bg='black')
c.pack(expand=NO)

bg = PhotoImage(file = img)
bg_img = c.create_image(0, 0, anchor=NW, image=bg)

def fig(event):
    x1,y1=(event.x-15),(event.y-15)
    x2,y2=(event.x+15),(event.y+15)
    c.create_oval(x1, y1, x2, y2, fill='white', outline='white')

def del_con(event):
    tk.title("Mask Canvas")
    plt.close('all')
    c.delete('all')
    bg_img

'''def img_con(event):
    global a
    global ar
    m = 3
    x, y = c.winfo_rootx(), c.winfo_rooty()
    w, h = c.winfo_width(), c.winfo_height()
    pyautogui.screenshot(str(a)+'.jpg', region=(x+m, y+m, w-m*2, h-m*2))
    img=cv2.imread(str(a)+'.jpg', cv2.IMREAD_GRAYSCALE)
    print(Fore.BLUE+Style.BRIGHT+str(np.shape(img))+Fore.RESET)
    img_=cv2.resize(img, dsize=(28,28), interpolation=cv2.INTER_AREA)
    print(np.shape(img_))
    cv2.imwrite(str(a)+'.jpg', img_)
    print("---->"+Fore.BLUE+Style.BRIGHT+str(a)+'.jpg'+Fore.RESET)
    ar=np.asarray(img_)
    plt.figure(figsize=[10,5])
    plt.subplot(121)
    plt.imshow(ar, cmap='gray')
    plt.show(block=False)
    a+=1
    c.delete('all')
    tk.title("Digit - "+str(a)[-1])'''

c.bind('<B1-Motion>', fig)
c.bind('<Button-3>', del_con)
#c.bind('<Button-2>', img_con)

tk.mainloop()