
from tkinter import *
from tkinter import filedialog
from PIL import Image

main_window = Tk()

def openFile():
    global filepath
    filepath = filedialog.askopenfilename()
    path.set(filepath)

def imageResize():
    img = Image.open(filepath)
    width = int(w1.get())
    height = int(h1.get())
    resized_img = img.resize((width,height))
    resized_img.save("d:/Album/resized_image.jpg")
    print("successful")

b1 = Button(main_window, text="load image", command=openFile)
b1.grid(row=0, column=0)

path = StringVar(main_window)
path.set("Choose file")

Label(main_window, textvariable=path).grid(row=0,column=1)

Label(main_window, text="input the dimensions").grid(row=1, column=0)

Label(main_window, text="Height: ").grid(row=2, column=0)

h1 = Entry(main_window, width=50, borderwidth=5)
h1.grid(row=2,column=1)

Label(main_window, text="Width: ").grid(row=2, column=2)

w1 = Entry(main_window, width=50, borderwidth=5)
w1.grid(row=2,column=3)

b2 = Button(main_window, text="convert", command=imageResize)
b2.grid(row=3,column=2)

main_window.mainloop()