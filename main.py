from cProfile import label
from tkinter import ttk
from tkinter import *
from turtle import width 
from tipoYeli import punt
from cmath import sqrt
import math
import random


class Giu:
    listPta = [[]]
    listCorde = [[]]
    def __init__(self, window):
        self.wind = window
        self.wind.title('Bombardo Perra')
        self.wind.geometry('605x460')
        self.wind.resizable(0,0) 
        self.wind.eval('tk::PlaceWindow . center')
        
        #Creando el frame Container
        frame = LabelFrame(self.wind, text = "Input Bombardeo")
        frame.grid(row = 0, column = 0, columnspan = 3,sticky=NSEW, padx = 10, pady = 5)
        
        
        #Creando el Frame Conaner table
        frameTable = LabelFrame(self.wind, text = "Tabla Iteraciones")
        frameTable.grid(row = 1, column = 0, columnspan = 3, sticky=NSEW, padx = 10, pady = 5)
        
        # Variable Iteraciones
        self.iterations = StringVar()
        self.novatos = StringVar()
        self.antiAerio = StringVar()
        # Numero de Iteraciones Input 
        Label(frame, text = "N° Iteraciones").grid(row = 2, column = 0)
        self.niteraciones = Entry(frame, width = 45, bd = 5, textvariable = self.iterations)
        self.niteraciones.grid(row = 2, column = 1, pady = 5, padx = 5)
        
        Label(frame, text = "Procentaje de los Bondaros Novatos").grid(row = 3, column = 0)
        self.pNovatos = Entry(frame, width = 45, bd = 5, textvariable = self.novatos)
        self.pNovatos.grid(row = 3, column = 1, pady = 5, padx = 5)
        
        Label(frame, text = "Porcentaje del antiaerio").grid(row = 4, column = 0)
        self.anti = Entry(frame, width = 45, bd = 5, textvariable = self.antiAerio)
        self.anti.grid(row = 4, column = 1, pady = 5, padx = 5)
        
        ttk.Button(frame, text = "Generar Simulacion", command = self.iteratorSimulator).grid(row = 5, columnspan = 2, sticky = W + E, pady = 5)
        
        #Table 
        self.tableColumns = ["N°","Tipo Bombardero", "Eliminado AntiAerio","Cordeada en X","Cordenada en Y"]
        self.tree = ttk.Treeview(frameTable, columns = self.tableColumns, show = "headings", height = 11)
        self.tree.heading("#1", text = "N°", anchor = "center")
        self.tree.heading("#2", text = "Tipo Bombardero", anchor = "center")
        self.tree.heading("#3", text = "Eliminado AntiAerio", anchor = "center")
        self.tree.heading("#4", text = "Cordeada en X", anchor = "center")
        self.tree.heading("#5", text = "Cordenada en Y", anchor = "center")
        
        # Tamaño de las columnas
        self.tree.column("#1", width = "50", stretch = False)
        self.tree.column("#2", width = "120",  stretch = False)
        self.tree.column("#3", width = "100",  stretch = False)
        self.tree.column("#4", width = "150",  stretch = False)
        self.tree.column("#5", width = "150", stretch = False)
        self.tree.grid(row = 2, column = 0, columnspan = 2, pady = 5, padx = 5)
    
    def iteracion(self):
        return self.iterations.get()
    
    def aleY(self):
        n = random.random()   
        return n

    def aleX(self):
        n = random.random()
        return n
    
    
    #coordenada Y
    def coordenadaY(self, pta):
        nIterations = int(self.iterations.get())
        for i in range ( nIterations ):  
        #pta = punt.tipoPersona()
    
            if  pta[1] == "No":
                res = "No le dio Alcastillo"
                #print("noCor",pta)
                return res  
            else: 
                if  pta[0] == "Novato" :
                    x = ( -math.log(random.random()))
                    y = (1/700)
                    res = (3 * math.pow(x,y)) 
                    #print("for1",pta)
                    return res * 100
                else:
                    #print("for2",pta)
                    res= ( -500 + ( math.sqrt(1000000 * self.aleY())))
                    return res

    def coordenaX(self, pta):
        if pta[1]== "No":
            res = "No le dio Alcastillo"
            #print("noCorX",pta)
            return res
        else:
            if  pta[0] == "Novato": 
                if self.aleX() <= 0.5:
                    resp = ( -600 + (sqrt(3920000 * random.random() ))  )
                    return resp
                else:
                    resp = ( 0 - (sqrt(1280000 * ( 1 - random.random() ))))
                    #print("forx2",pta)
                    return resp
            else:
                resp = (-600 + ( (600 - (-600)) * 0))
                #print("forx3",pta)
                return resp
    
    def guardarCorde(self, pta):
        coorY =  self.coordenadaY(pta)
        coorX =  self.coordenaX(pta)
        #arreglo 
        coordenadas = [coorY, coorX]
        return coordenadas


    
    def iteratorSimulator(self): 
        self.insertTable()
    
        
    def insertTable(self):
        novato = float(self.novatos.get())/100
        antiaerio = float(self.antiAerio.get())/100
        for i in range ( int(self.iterations.get()) ):
            pta = punt.tipoPersona(novato, antiaerio)
            self.listPta.append(pta) 
            self.listCorde.append(self.guardarCorde(pta))
            
        for i in range(1,int(self.iterations.get())):
            self.tree.insert("", 'end', values=(i, self.listPta[i][0], self.listPta[i][1],self.listCorde[i][0], self.listCorde[i][1]) )

if __name__ == '__main__':
    window = Tk()
    applications = Giu(window)
    window.mainloop()