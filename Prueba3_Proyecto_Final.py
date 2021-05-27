import tkinter
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk
import PIL


class Ventana:
    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Gráfica Polar")
        self.window.geometry("500x500+100+100")
        
        self.lbl01 = tkinter.Label(self.window, text = "X  =  ")
        self.lbl01.place(x = 10, y = 10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt01.place(x = 40, y = 10)

        self.lbl02 = tkinter.Label(self.window, text = "Y  =  ")
        self.lbl02.place(x = 10, y = 40)
        
        self.txt02 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt02.place(x = 40, y = 40) 
        
        #self.showGraph(self.txt01.get(), self.txt02.get())
        
        
        self.btn02 = tkinter.Button(self.window, text = "Mostrar", 
                                    command = self.btn02_click)
        self.btn02.place(x= 380, y=30, width=75)
        
        
        canvas = tkinter.Canvas(self.window, width = 350, height = 350)   
        canvas.place(x = 10, y = 100)
           
        img = ImageTk.PhotoImage(file="graph.png")

        #canvas.create_image(60,60, image=img)      


        imagen = PIL.Image.open("graph.png")
        width = 350
        height = 350
        im = imagen.resize((width, height), PIL.Image.ANTIALIAS)

        
        self.window.mainloop()
    #createWindow
        
    def makeGraph(self):
        
        lArr = np.array([3,2,3,2.5,3.8])
        x = lArr * 2
        lArr2 = np.array([6,7,1,3,4])
        y = lArr2 * np.pi
        area = (x**2) * 40
        color = np.random.rand(5)
        
        fig = plt.figure(dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        graph = ax.scatter(x, y, c = color, s = area, cmap = 'hsv', alpha = 0.75)
        plt.savefig('patas.png')
    #makeGraph()
        
    def showGraph(self):
        """
        root = tkinter.Tk()
        img = ImageTk.PhotoImage(Image.open("graph"))
        panel = tkinter.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        root.mainloop()
        """
        root = tkinter.Tk()      
        canvas = tkinter.Canvas(root, width = 300, height = 300)      
        canvas.pack()      
        img = ImageTk.PhotoImage(file="graph.png")      
        canvas.create_image(20,20, image=img)      
        root.mainloop()
        
    #showGraph()
        
    def btn01_click(self):
        self.makeGraph()
    # btn01_click
        
    def btn02_click(self):
        self.showGraph()
    # btn02_click        
        

#Ventana
        
myWin = Ventana()
myWin.createWindow()