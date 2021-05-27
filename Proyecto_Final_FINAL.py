import tkinter
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import os.path
plt.style.use('seaborn')

class main_window:
    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Gráfica Polar")
        self.window.geometry("745x425+150+120")
        
        self.lbl01 = tkinter.Label(self.window,
                                   text = "Cantidad de elementos  =  ")
        self.lbl01.config(font=("Century Gothic", 11))
        self.lbl01.place(x = 10, y = 10)
        
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width = 10,
                                   justify = "center")
        self.txt01.config(font = ("Century Gothic", 11))
        self.txt01.place(x = 190, y = 12)

        self.lbl_data = tkinter.Label(self.window, text = "Datos:")
        self.lbl_data.config(font=("Century Gothic", 11))
        self.lbl_data.place(x = 120, y = 50)
        
        self.btn_data_ran = tkinter.Button(self.window, text = "Aleatorio",
                                          command = self.btn_data_ran_clck)
        self.btn_data_ran.config(font=("Century Gothic", 11))
        self.btn_data_ran.place(x = 10, y = 80, width = 80)
        
        self.btn_data_in = tkinter.Button(self.window, text = "Ingresar",
                                         command = self.btn_data_in_clck)
        self.btn_data_in.config(font=("Century Gothic", 11))
        self.btn_data_in.place(x = 210, y = 80, width = 80)
        
        self.lbl_color = tkinter.Label(self.window,
                                       text = "Seleccione un tema de color:")
        self.lbl_color.config(font=("Century Gothic", 11))
        self.lbl_color.place(x = 40, y = 160)
        
        self.btn_color_ran = tkinter.Button(self.window, text = "Aleatorio",
                                            command = self.btn_color_ran_clck)
        self.btn_color_ran.config(font=("Century Gothic", 11))
        self.btn_color_ran.place(x = 10, y = 195, width = 80)
        
        self.btn_color_BN = tkinter.Button(self.window, text = "B/N",
                                           command = self.btn_color_BN_clck)
        self.btn_color_BN.config(font=("Century Gothic", 11))
        self.btn_color_BN.place(x = 110, y = 195, width = 80)
    
        self.btn_color_bl = tkinter.Button(self.window, text = "Azul",
                                           command = self.btn_color_bl_clck)
        self.btn_color_bl.config(font=("Century Gothic", 11))
        self.btn_color_bl.place(x = 210, y = 195, width = 80)
        
        self.btn_do = tkinter.Button(self.window, text = "Hacer",
                                     command = self.makeGraph)
        self.btn_do.config(font=("Century Gothic", 11))
        self.btn_do.place(x = 30, y = 280, width=75)
        
        self.btn_info = tkinter.Button(self.window, text = "Info",
                                       command = self.btn_info_clck)
        self.btn_info.config(font=("Century Gothic", 11))
        self.btn_info.place(x = 150, y = 280, width = 75)
        
        self.btn_shw_val = tkinter.Button(self.window, text = "Mostrar valores",
                                          command = self.btn_shw_val_clck)
        self.btn_shw_val.config(font=("Century Gothic", 11))
        self.btn_shw_val.place(x = 80, y = 330, width = 120)
        
        self.btn_reset = tkinter.Button(self.window, text = "RESET",
                                fg = "darkviolet", command = self.RESET_clck)
        self.btn_reset.config(font=("Century Gothic", 11))
        self.btn_reset.place(x = 80, y = 375, width = 120)
        
        self.graph_done = False
        
        self.window.mainloop()
    #createWindow()
        
    def btn_data_ran_clck(self):
        if(self.txt01.get() == ''):
            tkinter.messagebox.showinfo(title = "Aviso",
                        message="Favor de ingresar la cantdiad de elementos")
        else:            
            self.new_window = tkinter.Tk()
            self.new_window.title("Datos Aleatorios")
            self.new_window.geometry("235x160+100+100")
            lbl_range_x = tkinter.Label(self.new_window,
                                  text = "Rango de x\n(Grados °)")
            lbl_range_x.config(font=("Century Gothic", 11))
            lbl_range_x.place(x = 10, y = 10)
            
            lbl_range_x_equ = tkinter.Label(self.new_window, text = " = ")
            lbl_range_x_equ.config(font=("Century Gothic", 11))
            lbl_range_x_equ.place(x = 90, y = 20)
            
            self.txt_in_x = tkinter.Entry(self.new_window, bg = "lightgray",
                                       width = 5, justify = "center")
            self.txt_in_x.config(font=("Century Gothic", 11))
            self.txt_in_x.place(x = 115, y = 17)
            
            lbl_x_comma = tkinter.Label(self.new_window, text = ",")
            lbl_range_x.config(font=("Century Gothic", 11))
            lbl_x_comma.place(x = 165, y = 15)
            
            self.txt_in_x2 = tkinter.Entry(self.new_window, bg = "lightgray",
                                        width = 5, justify = "center")
            self.txt_in_x2.config(font=("Century Gothic", 11))
            self.txt_in_x2.place(x = 180, y = 17)
            
            lbl_range_y = tkinter.Label(self.new_window,
                                        text = "Rango de y\n(Distancia)")
            lbl_range_y.config(font=("Century Gothic", 11))
            lbl_range_y.place(x = 10, y = 63)
            
            lbl_range_y_equ = tkinter.Label(self.new_window, text = " = ")
            lbl_range_y_equ.config(font=("Century Gothic", 11))
            lbl_range_y_equ.place(x = 90, y = 73)
            
            self.txt_in_y = tkinter.Entry(self.new_window, bg = "lightgray",
                                       width = 5, justify = "center")
            self.txt_in_y.config(font=("Century Gothic", 11))
            self.txt_in_y.place(x = 115, y = 70)
            
            lbl_y_comma = tkinter.Label(self.new_window, text = ",")
            lbl_y_comma.config(font=("Century Gothic", 11))
            lbl_y_comma.place(x = 165, y = 65)
            
            self.txt_in_y2 = tkinter.Entry(self.new_window, bg = "lightgray",
                                        width = 5, justify = "center")
            self.txt_in_y2.config(font=("Century Gothic", 11))
            self.txt_in_y2.place(x = 180, y = 70)
            
            self.btn_ran_OK = tkinter.Button(self.new_window, text = "OK",
                                        command = self.OK_clck)
            self.btn_ran_OK.config(font=("Century Gothic", 11))
            self.btn_ran_OK.place(x = 80, y = 115, width = 50)
            
            self.OK_aux = 1

            self.new_window.mainloop()
    #btn_data_ran_clck()

    def btn_data_in_clck(self):
        if(self.txt01.get() == ''):
            tkinter.messagebox.showinfo(title = "Aviso",
                        message="Favor de ingresar la cantdiad de elementos")
        else:
            self.n = (int(self.txt01.get()))
            if(self.n > 10):
                self.n = 10
            y = self.n*30
            
            self.InputWindow = tkinter.Tk()
            self.InputWindow.title("Datos Puntuales")
            self.InputWindow.geometry("300x"+str(y+120))
            
            def CreateEntries(n):
                self.Entry_Y = []
                self.Entry_X = []
                self.New_Labels = []
                vertical = 40
                for i in range(0, n):
                    self.Entry_Y.append(tkinter.Entry(self.InputWindow,
                                                             width = 8))
                    self.Entry_X.append(tkinter.Entry(self.InputWindow,
                                                              width= 8))
                    self.New_Labels.append(tkinter.Label(self.InputWindow,
                                                         text = str(i+1)))
                    
                    self.Entry_Y[i].place(x = 60, y = vertical)
                    self.Entry_X[i].place(x = 180, y = vertical)
                    self.New_Labels[i].place(x = 10, y = vertical)
                    vertical += 32
            
            self.lbl_y_title = tkinter.Label(self.InputWindow, text = "Distancia")
            self.lbl_y_title.place(x = 60, y = 10)
            self.lbl_y_title.config(font=("Century Gothic", 11))
            
            self.lbl_x_title = tkinter.Label(self.InputWindow, text = "Grados")
            self.lbl_x_title.place(x = 180, y = 10)
            self.lbl_x_title.config(font=("Century Gothic", 11))
            
            #CREA N NÚMERO DE ENTRADAS
            Cantidad = int(self.txt01.get())
            if Cantidad > 10:
                Cantidad = 10
            CreateEntries(Cantidad)
            
            altura = Cantidad*31
            self.OK_aux = 0
            
            self.btn_in_OK = tkinter.Button(self.InputWindow, text = "OK",
                                            command = self.OK_clck)
            self.btn_in_OK.place(x = 40, y = altura+60)
            self.btn_in_OK.config(height = 2, width = 30)
            
            self.InputWindow.mainloop()
    #btn_data_in_clck()
        
    def btn_color_ran_clck(self):
        self.color_aux = 0
        self.color_sel = tkinter.Label(self.window,
                                       text = "Seleccionado: Aleatorio")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 260)
    #btn_color_ran_clck()

    def btn_color_BN_clck(self):
        self.color_aux = 1
        self.color_sel = tkinter.Label(self.window,
                                       text = "Seleccionado: Blanco y Negro")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 250)
    #btn_color_BN_clck()

    def btn_color_bl_clck(self):
        self.color_aux = 2
        self.color_sel = tkinter.Label(self.window, text = "Seleccionado: Azul")
        self.color_sel.config(font=("Century Gothic", 11), fg = "darkorchid")
        self.color_sel.place(x = 10, y = 242, width = 250)
    #btn_color_bl_clck() 
    
    def OK_clck (self):
        if(self.OK_aux == 1):
            if(self.txt_in_x.get() != '' and self.txt_in_x2.get() != '' and
               self.txt_in_y.get() != '' and self.txt_in_y2.get() != ''):
                tkinter.messagebox.showinfo(title = "OK",
                                    message = "Rangos Correctamente añadidos")
                self.str_to_num()
                self.new_window.destroy()
                self.sel_optn = tkinter.Label(self.window,
                                              text = "Seleccionado: Aleatorio")
                self.sel_optn.config(font=("Century Gothic", 11), fg = "darkorchid")
                self.sel_optn.place(x = 10, y = 130, width = 260)
            else:
                tkinter.messagebox.showinfo(title = "OK",
                                        message = "Favor de ingresar valores")
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
                tkinter.messagebox.showinfo(title = "OK",
                                    message = "Puntos Correctamente añadidos")
                self.InputWindow.destroy()
                self.sel_optn = tkinter.Label(self.window,
                                              text = "Seleccionado: Ingresar")
                self.sel_optn.config(font=("Century Gothic", 11), fg = "darkorchid")
                self.sel_optn.place(x = 10, y = 130, width = 260)
            else:
                tkinter.messagebox.showinfo(title = "OK",
                                                    message = "Faltan valores")
            self.aux_ok2 = 0
    #OK_clck()
        
    def open_img(self):
        if(os.path.exists(('graph.png'))):           
            img = Image.open('graph.png')
            img = img.resize((400, 400), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(self.window, image = img)
            panel.image = img
            panel.pack()
            panel.place(x = 330, y = 10)
            
            self.graph_done = True
        else:
            tkinter.messagebox.showinfo(title = "ERROR",
                            message = "No se guardó correctamente la gráfica")
    #open_img()

    def str_to_num(self):
        aux_X = self.txt_in_x.get()
        self.aux_x_1 = float(aux_X)
        aux_x2 = self.txt_in_x2.get()
        self.aux_x_2 = float(aux_x2)
        
        aux_Y = self.txt_in_y.get()
        self.aux_y_1 = float(aux_Y)
        aux2_Y = self.txt_in_y2.get()
        self.aux_y_2 = float(aux2_Y)
    #str_to_num()
        
    def color_select(self):
        if(self.color_aux == 0):
            self.color = np.random.rand(int(self.txt01.get()))
        elif(self.color_aux == 1):
            self.color = "gray"
        else:
            self.color = "lightskyblue"
    #color_select()
        
    def save_x_y(self):
        if(self.aux_ok2 == 1):
            self.x_2 = np.random.uniform(self.aux_x_1, self.aux_x_2,
                                                 size = int(self.txt01.get()))
            self.y_2 = np.random.uniform(self.aux_y_1, self.aux_y_2,                                                 size = int(self.txt01.get()))
    #save_x_y()
    
    def makeGraph(self): 
        self.color_select()
        self.save_x_y()
        self.y = self.y_2
        self.area = 40 * self.y
        self.x = self.x_2 * np.pi / 180
        fig = plt.figure(figsize = (2.7,2.7), dpi = 200)
        ax = fig.add_subplot(projection = 'polar')
        graph = ax.scatter(self.x, self.y, c = self.color, s = self.area,
                                                   cmap = 'hsv', alpha = 0.75)
        plt.savefig('graph.png')
        self.open_img()
    #makeGraph()
        
    def btn_info_clck(self):
        if(os.path.exists(('Info.png'))):           
            self.win_info = tkinter.Toplevel(self.window, height = 350, width = 350)
            self.win_info.title("Información")
            img_info = Image.open('Info.png')
            img_info = img_info.resize((350, 350), Image.ANTIALIAS)
            img_info = ImageTk.PhotoImage(img_info)
            panel_info = tkinter.Label(self.win_info, image = img_info)
            panel_info.image = img_info
            panel_info.pack()
            panel_info.place(x = 0, y = 0)
        else:
            tkinter.messagebox.showinfo(title = "ERROR",
                            message = "No se guardó la imagen de Información 'Info.png'")

    #btn_info_clck()
        
    def btn_shw_val_clck(self):
        if(self.graph_done == False):
            tkinter.messagebox.showinfo(title = "Aviso",
                                        message = "No se ha creado la gráfica")
        else:        
            self.new_window_2 = tkinter.Tk()
            self.new_window_2.title("Datos")
            self.new_window_2.geometry("600x425+100+100")
            
            self.lbl_val_x = tkinter.Label(self.new_window_2,
                                                      text = "Valores de\nx  ")
            self.lbl_val_x.config(font=("Century Gothic", 11))
            self.lbl_val_x.place(x = 10, y = 115)
            
            self.lbl_val_x_equ = tkinter.Label(self.new_window_2, text = "=")
            self.lbl_val_x_equ.config(font=("Century Gothic", 11))
            self.lbl_val_x_equ.place(x = 90, y = 127)
            
            self.data_x = tkinter.Text(self.new_window_2, bg = "lightgray",
                                                   width = 20, height = 12)
            self.data_x.config(font=("Century Gothic", 11), spacing1 = 3.5)
            self.data_x.place(x = 115, y = 15)
            
            self.lbl_val_y = tkinter.Label(self.new_window_2,
                                                       text = "Valores de\ny")
            self.lbl_val_y.config(font=("Century Gothic", 11))
            self.lbl_val_y.place(x = 315, y = 115)
            
            self.lbl_val_y_equ = tkinter.Label(self.new_window_2, text = "=")
            self.lbl_val_y_equ.config(font=("Century Gothic", 11))
            self.lbl_val_y_equ.place(x = 395, y = 127)
            
            self.data_y = tkinter.Text(self.new_window_2, bg = "lightgray",
                                                       width = 20, height = 12)
            self.data_y.config(font=("Century Gothic", 11), spacing1 = 3.5)
            self.data_y.place(x = 420, y = 15)
            
            self.lbl_area_circ = tkinter.Label(self.new_window_2,
                                               text = "Área de\ncada círculo")
            self.lbl_area_circ.config(font = ("Century Gothic", 11))
            self.lbl_area_circ.place(x = 10, y = 340)
            
            self.lbl_area_circ_2_equ = tkinter.Label(self.new_window_2, text = "=")
            self.lbl_area_circ_2_equ.config(font=("Century Gothic", 11))
            self.lbl_area_circ_2_equ.place(x = 93, y = 346)
            
            self.data_area = tkinter.Text(self.new_window_2, bg = "lightgray",
                                                       width = 58, height = 6)
            self.data_area.config(font = ("Century Gothic", 11))
            self.data_area.place(x = 116, y = 306)
            
            self.data_hist()
            
            self.new_window_2.mainloop()
    #btn_shw_val_clck()
            
    def data_hist(self):
        x_aux = ""
        x_x = self.x_2
        for val_x in x_x:
            aux_x2 = "{}\n".format(val_x)
            x_aux += aux_x2
        self.data_x.insert("end", x_aux)
        
        y_aux = ""
        y_y = self.y_2
        y_y = self.y
        for val_y in y_y:
            aux2_y = "{}\n".format(val_y)
            y_aux += aux2_y
        self.data_y.insert("end", y_aux)
        
        a_aux = ""
        a_area = self.area
        for val_a in a_area:
            aux2_a = "{}  ".format(val_a)
            a_aux += aux2_a
        self.data_area.insert("end", a_aux)
    #data_hist()
        
    def RESET_clck(self):
        self.window.destroy()
        self.createWindow()
    #RESET()
        
#Ventana
        
myWin = main_window()
myWin.createWindow()
