import customtkinter
from PIL import Image
import os
current_path = os.path.realpath(os.path.dirname(__file__))

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("ImageResizer by Aniket")

path = customtkinter.StringVar(root)
path.set("Choose file")

def openFile():
    global filepath
    filepath = customtkinter.filedialog.askopenfilename()
    path.set(filepath)

def imageResize():
    img = Image.open(filepath)
    width = int(e2.get())
    height = int(e1.get())
    resized_img = img.resize((width,height))
    resized_img.save(current_path+"/resized_image.jpg")
    result.set("Image saved")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

b1 = customtkinter.CTkButton(master=frame, text="load image", command=openFile)
b1.grid(pady=10, padx=20, row=0, column=0)

l1 = customtkinter.CTkLabel(master=frame, textvariable=path)
l1.grid(pady=10, padx=20, row=0, column=1)

l2 = customtkinter.CTkLabel(master=frame, text="Height: ")
l2.grid(pady=10, padx=20, row=2, column=0)

e1 = customtkinter.CTkEntry(master=frame)
e1.grid(pady=10, padx=20, row=2,column=1)

l3 = customtkinter.CTkLabel(master=frame, text="Width: ")
l3.grid(pady=10, padx=20, row=3, column=0)

e2 = customtkinter.CTkEntry(master=frame)
e2.grid(pady=10, padx=20, row=3,column=1)

b2 = customtkinter.CTkButton(master=frame, text="resize", command=imageResize)
b2.grid(pady=10, padx=20, row=4,column=0)

result = customtkinter.StringVar(root)
l4 = customtkinter.CTkLabel(master=frame, textvariable=result)
l4.grid(pady=10, padx=20, row=4,column=1)

root.mainloop()