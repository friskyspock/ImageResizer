# ImageResizer
A simple program that can resize images quickly

We often ran into issues where we have to upload our passport size image for an application on a institutional websites. This websites only accept certain pixel dimensions. To achieve them, we usually run to MSPaint or online image editors. To make this process easier, I have made this simple application.

You just have to download ImageResizer2.exe file and enjoty
Note that program will save image in current directory of your application. The name of file will be "resized_image.jpg". To see my source python code checkout "ImageResizer2.py". There is sample image and resized image included in repository.

I used customtinker python package to make my gui app and made exe file using pyinstaller. For image manipulation, python package PIL is used.

Pyinstaller has some issues with customtkinter. To see them visit:
https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging#windows-pyinstaller-auto-py-to-exe