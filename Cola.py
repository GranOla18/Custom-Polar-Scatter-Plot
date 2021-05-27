import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


class Ventana:
    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Gráfica Polar")
        self.window.geometry("500x500+100+100")
        
        self.makeGraph()
        
        self.image = tkinter.Button(self.window, text='open image', command=self.open_img).pack()
        
        self.lbl01 = tkinter.Label(self.window, text = "Cantidad de elementos  =  ")
        self.lbl01.place(x = 10, y = 10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt01.place(x = 4, y = 10)
        #Pedir cantidad de bolitas
        #Botones con paletas de colores (color especifico (tonos) // random)
        #
        
        self.window.mainloop()
    #createWindow
        
    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename
    
    def open_img(self):
        img = Image.open('patas.png')
        img = img.resize((500, 330), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.window, image=img)
        panel.image = img
        panel.pack()
    
    #showGraph()

    def makeGraph(self):
        N = 10
        #lArr = np.array([3,2,3,2.5,3.8])
        x = 2 * np.pi * np.random.rand(N)
        #lArr2 = np.array([6,7,1,3,4])
        y = 2 * np.pi * np.random.rand(N)
        area = 20 * x**2
        color = np.random.rand(N)
        fig = plt.figure(dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        graph = ax.scatter(x, y, c = color, s = area, cmap = 'hsv', alpha = 0.75)
        plt.savefig('patas.png')
    #makeGraph
       
        

#Ventana
        
myWin = Ventana()
myWin.createWindow()
