import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.

from matplotlib.figure import Figure

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt

class Ventana:
    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Gráfica Polar")
        self.window.geometry("600x560+100+100")
        
        self.lbl01 = tkinter.Label(self.window, text = "Cantidad de elementos  =  ")
        self.lbl01.config(font=("Century Gothic", 11))
        self.lbl01.place(x = 10, y = 10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width = 10, justify = "center")
        self.txt01.config(font = ("Century Gothic", 11))
        self.txt01.place(x = 190, y = 12)
        
        self.lbl02 = tkinter.Label(self.window, text = "Rango de x =  ")
        self.lbl02.config(font=("Century Gothic", 11))
        self.lbl02.place(x = 10, y = 40)
        
        self.txt_X = tkinter.Entry(self.window, bg = "lightgray", width = 5, justify = "center")
        self.txt_X.config(font=("Century Gothic", 11))
        self.txt_X.place(x = 105, y = 42)
        
        self.lbl03 = tkinter.Label(self.window, text = ",")
        self.lbl02.config(font=("Century Gothic", 11))
        self.lbl03.place(x = 155, y = 40)
        
        self.txt_X2 = tkinter.Entry(self.window, bg = "lightgray", width = 5, justify = "center")
        self.txt_X2.config(font=("Century Gothic", 11))
        self.txt_X2.place(x = 170, y = 42)
        
        self.lbl04 = tkinter.Label(self.window, text = "Rango de y =  ")
        self.lbl04.config(font=("Century Gothic", 11))
        self.lbl04.place(x = 10, y = 70)
        
        self.txt_Y = tkinter.Entry(self.window, bg = "lightgray", width = 5, justify = "center")
        self.txt_Y.config(font=("Century Gothic", 11))
        self.txt_Y.place(x = 105, y = 72)
        
        self.lbl05 = tkinter.Label(self.window, text = ",")
        self.lbl05.config(font=("Century Gothic", 11))
        self.lbl05.place(x = 155, y = 70)
        
        self.txt_Y2 = tkinter.Entry(self.window, bg = "lightgray", width = 5, justify = "center")
        self.txt_Y2.config(font=("Century Gothic", 11))
        self.txt_Y2.place(x = 170, y = 72)
        
        self.btn01 = tkinter.Button(self.window, text = "Hacer", 
                                    command = self.makeGraph)
        self.btn01.config(font=("Century Gothic", 11))
        self.btn01.place(x = 30, y = 115, width=75)
        
        self.btn02 = tkinter.Button(self.window, text = "Info", command = self.btn_info)
        self.btn02.config(font=("Century Gothic", 11))
        self.btn02.place(x = 150, y = 115, width = 75)
        
        self.lbl06 = tkinter.Label(self.window, text = "Valores de\nx  ")
        self.lbl06.config(font=("Century Gothic", 11))
        self.lbl06.place(x = 10, y = 271)
        
        self.lbl06_2 = tkinter.Label(self.window, text = "=")
        self.lbl06_2.config(font=("Century Gothic", 11))
        self.lbl06_2.place(x = 90, y = 283)
        
        self.data_x = tkinter.Text(self.window, bg = "lightgray", width = 20, height = 12)
        self.data_x.config(font=("Century Gothic", 11), spacing1 = 3.5)
        self.data_x.place(x = 115, y = 165)
        
        self.lbl07 = tkinter.Label(self.window, text = "Valores de\ny")
        self.lbl07.config(font=("Century Gothic", 11))
        self.lbl07.place(x = 315, y = 271)
        
        self.lbl07_2 = tkinter.Label(self.window, text = "=")
        self.lbl07_2.config(font=("Century Gothic", 11))
        self.lbl07_2.place(x = 395, y = 283)
        
        self.data_y = tkinter.Text(self.window, bg = "lightgray", width = 20, height = 12)
        self.data_y.config(font=("Century Gothic", 11), spacing1 = 3.5)
        self.data_y.place(x = 420, y = 160)
        
        self.lbl08 = tkinter.Label(self.window, text = "Área de\ncada bolita")
        self.lbl08.config(font = ("Century Gothic", 11))
        self.lbl08.place(x = 10, y = 475)
        
        self.lbl08_2 = tkinter.Label(self.window, text = "=")
        self.lbl08_2.config(font=("Century Gothic", 11))
        self.lbl08_2.place(x = 95, y = 480)
        
        self.data_a = tkinter.Text(self.window, bg = "lightgray", width = 58, height = 6)
        self.data_a.config(font = ("Century Gothic", 11))
        self.data_a.place(x = 120, y = 440)
        
        #self.image = tkinter.Button(self.window, text='open image', command=self.open_img)
        #self.image.place(x = 200, y = 400)
        
        self.window.mainloop()
    #createWindow
        
    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename
    
    def open_img(self, file_name, where):
        img = Image.open(file_name)
        img2 = img.resize((300, 300), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        panel = tkinter.Label(where, image=img2)
        panel.image = img2
        panel.pack()
    #open_img()

    def str_to_num(self):
        aux_N = self.txt01.get()
        self.aux2_N = int(aux_N)
        aux_X = self.txt_X.get()
        self.aux_X_1 = float(aux_X)
        aux2_X = self.txt_X2.get()
        self.aux_x_2 = float(aux2_X)
        aux_Y = self.txt_Y.get()
        self.aux_Y_1 = float(aux_Y)
        aux2_Y = self.txt_Y2.get()
        self.aux_Y_2 = float(aux2_Y)
    #str_to_num
        
    def data_hist(self):
        x_aux = ""
        x_x = self.x
        for val_x in x_x:
            aux2_x = "{}\n".format(val_x)
            x_aux += aux2_x
        #x_aux = "{}".format(self.x)
        self.data_x.insert("end", x_aux)
        
        y_aux = ""
        y_y = self.y
        for val_y in y_y:
            aux2_y = "{}\n".format(val_y)
            y_aux += aux2_y
        #y_aux = "{}".format(self.y)
        self.data_y.insert("end", y_aux)
        
        a_aux = ""
        a_area = self.area
        for val_a in a_area:
            aux2_a = "{}  ".format(val_a)
            a_aux += aux2_a
        self.data_a.insert("end", a_aux)
    
    def makeGraph(self): 
        self.str_to_num()
        N = self.aux2_N
        #lArr = np.array([3,2,3,2.5,3.8])
        self.x = np.random.uniform(self.aux_X_1, self.aux_x_2, size = N) * np.pi / 180
        #lArr2 = np.array([6,7,1,3,4])
        self.y = np.random.uniform(self.aux_Y_1, self.aux_Y_2, size = N)
        print(self.aux_Y_1)
        print(self.aux_Y_2)
        self.area = 10 * self.y
        color = np.random.rand(N)
        fig = plt.figure(figsize = (2.7,2.7), dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        graph = ax.scatter(self.x, self.y, c = color, s = self.area, cmap = 'hsv', alpha = 0.75)
        #plt.savefig('graph.png')
        
        canvas = FigureCanvasTkAgg(fig, master=tkinter.Tk())  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
        self.data_hist()
    #makeGraph
        
    def btn_info(self):
        self.win_info = tkinter.Toplevel(self.window, height = 300, width = 500)
        self.win_info.title("Información")
        self.open_img('Pixel_Art_2_1.gif', self.win_info)
        

        

#Ventana
        
myWin = Ventana()
myWin.createWindow()
