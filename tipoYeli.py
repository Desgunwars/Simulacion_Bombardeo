import random

def aleTB():
    n = random.random()
    return n

def aleEA():
    n = random.random()
    return n
#-----------------------------------------
#Tipo de Bombardero
def tipoBombardero(novatos):
    if aleTB() <= novatos:
        return "Novato"
    else:
        return "Veterano"
#Eliminado por antiaereo
def eliminadoPorAnti(antiaerio):
    if aleEA() <= antiaerio:
        return "Si"
    else:
        return "No"
#-------------------------------------------
#guardadon el bombardero en un arreglo
class punt:
    def tipoPersona(novatos, antiaerio):
        tipo1=  tipoBombardero(novatos)
        elmiEA1 = eliminadoPorAnti(antiaerio)
        #arreglo 
        interacion =[tipo1, elmiEA1]
        return interacion
#------------------------------------

