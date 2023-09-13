import os
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from colorama import Fore, Style
from PIL import Image, ImageTk, ImageDraw

tk = Tk()
os.chdir("testImages")
inImg = "1.jpg"

tk.title("Mask Canvas")
c=Canvas(tk, width=1024, height=1024, bg='black')
c.pack(expand=NO)

bg = ImageTk.PhotoImage(Image.open(inImg))
bg_img = c.create_image(0, 0, anchor=NW, image=bg)

img = Image.new("L", (1024, 1024), "black")
draw = ImageDraw.Draw(img)

def fig(event):
    x1,y1=(event.x-15),(event.y-15)
    x2,y2=(event.x+15),(event.y+15)
    c.create_oval(x1, y1, x2, y2, fill='white', outline='white', tags='overlay')
    draw.ellipse([x1, y1, x2, y2], fill='white', outline='white')
22
def del_con(event):
    tk.title("Mask Canvas")
    plt.close('all')
    c.delete('overlay')

def img_con(event):
    c.delete(bg_img)
    c.update()
    outImg = '_Mask.'.join(inImg.split('.'))
    print(Fore.BLUE+Style.BRIGHT+"---->"+outImg+Fore.RESET)
    
    img_ar = np.array(img)
    print('----------------->',img_ar.shape)
    plt.imshow(img_ar, cmap='gray')
    plt.show(block=False)
    img.save(outImg)

c.bind('<B1-Motion>', fig)
c.bind('<Button-3>', del_con)
c.bind('<Button-2>', img_con)

tk.mainloop()