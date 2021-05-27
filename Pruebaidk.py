import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog

root = tkinter.Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    img = Image.open('graph.png')
    img = img.resize((500, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tkinter.Label(root, image=img)
    panel.image = img
    panel.pack()

btn = tkinter.Button(root, text='open image', command=open_img).pack()

root.mainloop()
