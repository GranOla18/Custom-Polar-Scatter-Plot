import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import os.path

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
        self.window.geometry("745x425+100+100")
        
        self.lbl01 = tkinter.Label(self.window, text = "Cantidad de elementos  =  ")
        self.lbl01.config(font=("Century Gothic", 11))
        self.lbl01.place(x = 10, y = 10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width = 10, justify = "center")
        self.txt01.config(font = ("Century Gothic", 11))
        self.txt01.place(x = 190, y = 12)
        
        self.btn01 = tkinter.Button(self.window, text = "Hacer", 
                                    command = self.makeGraph)
        self.btn01.config(font=("Century Gothic", 11))
        self.btn01.place(x = 30, y = 280, width=75)
        
        self.btn02 = tkinter.Button(self.window, text = "Info", command = self.btn_info_clck)
        self.btn02.config(font=("Century Gothic", 11))
        self.btn02.place(x = 150, y = 280, width = 75)
        
        self.lbl10 = tkinter.Label(self.window, text = "Datos:")
        self.lbl10.config(font=("Century Gothic", 11))
        self.lbl10.place(x = 120, y = 50)
        
        self.btn06 = tkinter.Button(self.window, text = "Aleatorio", command = self.btn06_clck)
        self.btn06.config(font=("Century Gothic", 11))
        self.btn06.place(x = 10, y = 80, width = 80)
        
        self.btn07 = tkinter.Button(self.window, text = "Ingresar", command = self.btn07_clck)
        self.btn07.config(font=("Century Gothic", 11))
        self.btn07.place(x = 210, y = 80, width = 80)
        
        self.lbl09 = tkinter.Label(self.window, text = "Seleccione un tema de colores: ")
        self.lbl09.config(font=("Century Gothic", 11))
        self.lbl09.place(x = 40, y = 160)
        
        self.btn03 = tkinter.Button(self.window, text = "Aleatorio", command = self.btn03_clck)
        self.btn03.config(font=("Century Gothic", 11))
        self.btn03.place(x = 10, y = 195, width = 80)
        
        self.btn04 = tkinter.Button(self.window, text = "B/N", command = self.btn04_clck)
        self.btn04.config(font=("Century Gothic", 11))
        self.btn04.place(x = 110, y = 195, width = 80)
    
        self.btn05 = tkinter.Button(self.window, text = "Azul", command = self.btn05_clck)
        self.btn05.config(font=("Century Gothic", 11))
        self.btn05.place(x = 210, y = 195, width = 80)
        
        self.btn08 = tkinter.Button(self.window, text = "Mostrar valores", command = self.btn08_clck)
        self.btn08.config(font=("Century Gothic", 11))
        self.btn08.place(x = 80, y = 330, width = 120)
        
        self.btn10 = tkinter.Button(self.window, text = "RESET", fg = "darkviolet", command = self.RESET_clck)
        self.btn10.config(font=("Century Gothic", 11))
        self.btn10.place(x = 80, y = 375, width = 120)
        
        self.graph_done = False
        
        
        #self.image = tkinter.Button(self.window, text='open image', command=self.open_img)
        #self.image.place(x = 200, y = 400)
        
        self.window.mainloop()
    #createWindow
        
    def btn03_clck(self):
        self.color_aux = 0
        self.color_sel = tkinter.Label(self.window, text = "Seleccionado: Aleatorio")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 260)
    #btn03

    def btn04_clck(self):
        self.color_aux = 1
        self.color_sel = tkinter.Label(self.window, text = "Seleccionado: Blanco y Negro")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 250)
    #btn04

    def btn05_clck(self):
        self.color_aux = 2
        self.color_sel = tkinter.Label(self.window, text = "Seleccionado: Azul")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 250)
    #btn05   
        
    def btn06_clck(self):
        if(self.txt01.get() == ''):
            tkinter.messagebox.showinfo(title = "Aviso", message="Favor de ingresar la cantdiad de elementos")
        else:            
            self.new_window = tkinter.Tk()
            self.new_window.title("Datos")
            self.new_window.geometry("235x160+100+100")
            lbl02 = tkinter.Label(self.new_window, text = "Rango de x\n(Grados °)")
            lbl02.config(font=("Century Gothic", 11))
            lbl02.place(x = 10, y = 10)
            
            lbl02_equ = tkinter.Label(self.new_window, text = " = ")
            lbl02_equ.config(font=("Century Gothic", 11))
            lbl02_equ.place(x = 90, y = 20)
            
            self.txt_X = tkinter.Entry(self.new_window, bg = "lightgray", width = 5, justify = "center")
            self.txt_X.config(font=("Century Gothic", 11))
            self.txt_X.place(x = 115, y = 17)
            
            lbl03 = tkinter.Label(self.new_window, text = ",")
            lbl02.config(font=("Century Gothic", 11))
            lbl03.place(x = 165, y = 15)
            
            self.txt_X2 = tkinter.Entry(self.new_window, bg = "lightgray", width = 5, justify = "center")
            self.txt_X2.config(font=("Century Gothic", 11))
            self.txt_X2.place(x = 180, y = 17)
            
            lbl04 = tkinter.Label(self.new_window, text = "Rango de y\n(Distancia)")
            lbl04.config(font=("Century Gothic", 11))
            lbl04.place(x = 10, y = 63)
            
            lbl04_equ = tkinter.Label(self.new_window, text = " = ")
            lbl04_equ.config(font=("Century Gothic", 11))
            lbl04_equ.place(x = 90, y = 73)
            
            self.txt_Y = tkinter.Entry(self.new_window, bg = "lightgray", width = 5, justify = "center")
            self.txt_Y.config(font=("Century Gothic", 11))
            self.txt_Y.place(x = 115, y = 70)
            
            lbl05 = tkinter.Label(self.new_window, text = ",")
            lbl05.config(font=("Century Gothic", 11))
            lbl05.place(x = 165, y = 65)
            
            self.txt_Y2 = tkinter.Entry(self.new_window, bg = "lightgray", width = 5, justify = "center")
            self.txt_Y2.config(font=("Century Gothic", 11))
            self.txt_Y2.place(x = 180, y = 70)
            
            self.btn09 = tkinter.Button(self.new_window, text = "OK", command = self.OK_clck)
            self.btn09.config(font=("Century Gothic", 11))
            self.btn09.place(x = 80, y = 115, width = 50)
            
            """
            self.color_sel_d = tkinter.Label(self.window, text = "Seleccionado: Aleatorio")
            self.color_sel_d.config(font=("Century Gothic", 11), fg = "darkorchid")
            self.color_sel_d.place(x = 10, y = 125, width = 260)
            """
            self.OK_aux = 1

            
            self.new_window.mainloop()
    #btn06
    
    def OK_clck (self):
        if(self.OK_aux == 1):
            if(self.txt_X.get() != '' and self.txt_X2.get() != '' and self.txt_Y.get() != '' and self.txt_Y2.get() != ''):
                tkinter.messagebox.showinfo(title = "OK", message="Rangos Correctamente añadidos")
                self.str_to_num()
                self.new_window.destroy()
                self.color_sel_d = tkinter.Label(self.window, text = "Seleccionado: Aleatorio")
                self.color_sel_d.config(font=("Century Gothic", 11), fg = "darkorchid")
                self.color_sel_d.place(x = 10, y = 130, width = 260)
            else:
                tkinter.messagebox.showinfo(title = "OK", message="Favor de ingresar valores")
            self.aux_ok2 = 1
        elif(self.OK_aux == 0):
            for i in range(0, int(self.txt01.get())):
                if((self.Entry_Y[i].get()) != ''):
                    aux_ok = True
                elif((self.Entry_X[i].get()) != ''):
                    aux_ok = True
                elif((self.Entry_Y[i].get()) == ''):
                    aux_ok = False  
                elif((self.Entry_X[i].get()) != ''):
                    aux_ok = False
            if(aux_ok == True):
                self.dataY = []
                self.dataX = []
                for i in range(0, int(self.txt01.get())):
                    self.dataY.append(int(self.Entry_Y[i].get()))
                    self.dataX.append(int(self.Entry_X[i].get()))
                self.x_2 = np.array(self.dataX)
                self.y_2 = np.array(self.dataY)
                self.ran = False
                tkinter.messagebox.showinfo(title = "OK", message = "Puntos Correctamente añadidos")
                self.InputWindow.destroy()
                self.color_sel_d = tkinter.Label(self.window, text = "Seleccionado: Ingresar")
                self.color_sel_d.config(font=("Century Gothic", 11), fg = "darkorchid")
                self.color_sel_d.place(x = 10, y = 130, width = 260)
            else:
                tkinter.messagebox.showinfo(title = "OK", message = "Faltan valores")
            self.aux_ok2 = 0
    #OK
        
    
    def btn07_clck(self):
        if(self.txt01.get() == ''):
            tkinter.messagebox.showinfo(title = "Aviso", message="Favor de ingresar la cantdiad de elementos")
        else:
            self.n = (int(self.txt01.get()))
            if(self.n > 10):
                self.n = 10
            y = self.n*30
            
            self.InputWindow = tkinter.Tk()
            self.InputWindow.title("Ingresar Puntos")
            self.InputWindow.geometry("300x"+str(y+120))
            
            def CreateEntries(n):
                self.Entry_Y = []
                self.Entry_X = []
                self.New_Labels = []
                vertical = 40
                for i in range(0, n):
                    self.Entry_Y.append(tkinter.Entry(self.InputWindow,width = 8))
                    self.Entry_X.append(tkinter.Entry(self.InputWindow,width= 8))
                    self.New_Labels.append(tkinter.Label(self.InputWindow, text = str(i+1)))
                    
                    self.Entry_Y[i].place(x = 60, y = vertical)
                    self.Entry_X[i].place(x = 180, y = vertical)
                    self.New_Labels[i].place(x = 10, y = vertical)
                    vertical += 32
            
            #print(self.Entry_Y)
            self.Label_R = tkinter.Label(self.InputWindow, text = "Distancia")
            self.Label_R.place(x = 60, y = 10)
            self.Label_R.config(font=("Century Gothic", 11))
            
            self.Label_Theta = tkinter.Label(self.InputWindow, text = "Grados")
            self.Label_Theta.place(x = 180, y = 10)
            self.Label_Theta.config(font=("Century Gothic", 11))
            
            #CREA N NÚMERO DE ENTRADAS
            Cantidad = int(self.txt01.get())
            if Cantidad > 10:
                Cantidad = 10
            CreateEntries(Cantidad)
            
            altura = Cantidad*31
            self.OK_aux = 0
            
            self.OK = tkinter.Button(self.InputWindow,text = "OK", command=self.OK_clck)
            self.OK.place(x = 40, y = altura+60)
            self.OK.config(height = 2, width = 30)
            
            """ 
            self.color_sel_d = tkinter.Label(self.window, text = "Seleccionado: Ingresar")
            self.color_sel_d.config(font=("Century Gothic", 11), fg = "darkorchid")
            self.color_sel_d.place(x = 10, y = 130, width = 260)
            """
            self.InputWindow.mainloop()
        
    #btn07
        
    #Valores Aleatorios
    def btn08_clck(self):
                
        if(self.graph_done == False):
            tkinter.messagebox.showinfo(title = "Aviso", message="No se ha creado la gráfica")
        else:        
            self.new_window_2 = tkinter.Tk()
            self.new_window_2.title("Datos")
            self.new_window_2.geometry("600x425+100+100")
            
            self.lbl06 = tkinter.Label(self.new_window_2, text = "Valores de\nx  ")
            self.lbl06.config(font=("Century Gothic", 11))
            self.lbl06.place(x = 10, y = 115)
            
            self.lbl06_2 = tkinter.Label(self.new_window_2, text = "=")
            self.lbl06_2.config(font=("Century Gothic", 11))
            self.lbl06_2.place(x = 90, y = 127)
            
            self.data_x = tkinter.Text(self.new_window_2, bg = "lightgray", width = 20, height = 12)
            self.data_x.config(font=("Century Gothic", 11), spacing1 = 3.5)
            self.data_x.place(x = 115, y = 15)
            
            self.lbl07 = tkinter.Label(self.new_window_2, text = "Valores de\ny")
            self.lbl07.config(font=("Century Gothic", 11))
            self.lbl07.place(x = 315, y = 115)
            
            self.lbl07_2 = tkinter.Label(self.new_window_2, text = "=")
            self.lbl07_2.config(font=("Century Gothic", 11))
            self.lbl07_2.place(x = 395, y = 127)
            
            self.data_y = tkinter.Text(self.new_window_2, bg = "lightgray", width = 20, height = 12)
            self.data_y.config(font=("Century Gothic", 11), spacing1 = 3.5)
            self.data_y.place(x = 420, y = 15)
            
            self.lbl08 = tkinter.Label(self.new_window_2, text = "Área de\ncada bolita")
            self.lbl08.config(font = ("Century Gothic", 11))
            self.lbl08.place(x = 10, y = 340)
            
            self.lbl08_2 = tkinter.Label(self.new_window_2, text = "=")
            self.lbl08_2.config(font=("Century Gothic", 11))
            self.lbl08_2.place(x = 93, y = 346)
            
            self.data_a = tkinter.Text(self.new_window_2, bg = "lightgray", width = 58, height = 6)
            self.data_a.config(font = ("Century Gothic", 11))
            self.data_a.place(x = 116, y = 306)
            
            self.data_hist()
            
            self.new_window_2.mainloop()
        
    
    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename
    
    def open_img(self):
        if(os.path.exists(('graph.png'))):           
            self.img = Image.open('graph.png')
            self.img = self.img.resize((400, 400), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            self.panel = tkinter.Label(self.window, image=self.img)
            self.panel.image = self.img
            self.panel.pack()
            self.panel.place(x = 330, y = 10)
            self.graph_done = True
        else:
            tkinter.messagebox.showinfo(title = "ERROR", message = "No se guardo correctamente la gráfica")
            
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
        if(self.ran == True):
            x_x = self.x_2
            print(self.x_2)
        elif(self.ran == False):
            x_x = self.x_2
        #x_x = self.x
        for val_x in x_x:
            aux2_x = "{}\n".format(val_x)
            x_aux += aux2_x
        #x_aux = "{}".format(self.x)
        self.data_x.insert("end", x_aux)
        print(self.data_x)
        
        y_aux = ""
        if(self.ran == True):
            y_y = self.y_2
        else:
            y_y = self.y_2
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
        self.colores()
        #N = self.aux2_N
        self.save_x_y()
        #self.x = 2 * np.pi * np.random.uniform(self.aux_X_1, self.aux_x_2, size = N)
        #lArr2 = np.array([6,7,1,3,4])
        #self.y = 2 * np.pi * np.random.uniform(self.aux_Y_1, self.aux_Y_2, size = N)
        self.y = self.y_2
        #print(self.y)
        self.area = 40 * self.y
        #color = np.random.rand(N)
        #x = self.y * 180 / np.pi
        self.x = self.x_2 * np.pi / 180
        #print(self.x)
        #print(self.x)
        fig = plt.figure(figsize = (2.7,2.7), dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        graph = ax.scatter(self.x, self.y, c = self.color, s = self.area, cmap = 'hsv', alpha = 0.75)
        plt.savefig('graph.png')
        #canvas = FigureCanvasTkAgg(fig, master=tkinter.Tk())  # A tk.DrawingArea.
        #canvas.draw()
        #canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
        self.open_img()
        
    #makeGraph
    
    
    def save_x_y(self):
        #self.OK_clck()
        if(self.aux_ok2 == 1):
            self.x_2 = np.random.uniform(self.aux_X_1, self.aux_x_2, size = int(self.txt01.get()))
            self.y_2 = np.random.uniform(self.aux_Y_1, self.aux_Y_2, size = int(self.txt01.get()))
            self.ran = True
        
    def colores(self):
        if(self.color_aux == 0):
            self.color = np.random.rand(int(self.txt01.get()))
        elif(self.color_aux == 1):
            self.color = "gray"
        else:
            self.color = "lightskyblue"
    #colores
    
    def btn_info_clck(self):
        self.win_info = tkinter.Toplevel(self.window, height = 405, width = 400)
        self.win_info.title("Información")
        img = Image.open('Info.png')
        img = img.resize((400, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.win_info, image=img)
        panel.image = img
        panel.pack()
        panel.place(x = 0, y = 0)
        
    def RESET_clck(self):
        self.window.destroy()
        self.createWindow()
        

#Ventana
        
myWin = Ventana()
myWin.createWindow()
