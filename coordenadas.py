from cmath import sqrt
import math
import random
from tipoYeli import punt

    


def iteracion():
    return 50 

def aleY():
   n = random.random()   
   return n

def aleX():
    n = random.random()
    return n
#-----------------------------

#coordenada Y
def coordenadaY():
 for i in range ( iteracion() ):  
    #pta = punt.tipoPersona()
    
    if  pta[1] == "No":
        res = "No-coordenada"
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
            res= ( -500 + ( math.sqrt(1000000 * aleY())))
            return res

def coordenaX():
    if pta[1]== "No":
        res = "No-coordenada"
        #print("noCorX",pta)
        return res
    else:
        if  pta[0] == "Novato": 
             if aleX() <= 0.5:
                resp = ( -600 + (sqrt(3920000 * random.random() ))  )
               # print("forx1",pta)
                return resp
             else:
                resp = ( 0 - (sqrt(1280000 * ( 1 - random.random() ))))
                #print("forx2",pta)
                return resp
        else:
            resp = (-600 + ( (600 - (-600)) * 0))
            #print("forx3",pta)
            return resp

#guardar las coordenadas en un arreglo
def guardarCorde():
    coorY =  coordenadaY()
    coorX =  coordenaX()
    #arreglo 
    coordenadas = [coorY, coorX]
    return coordenadas



# inicializando el programa
for i in range ( iteracion() ):
    pta = punt.tipoPersona()
    print(pta)
    print (guardarCorde())
    print("*****************")