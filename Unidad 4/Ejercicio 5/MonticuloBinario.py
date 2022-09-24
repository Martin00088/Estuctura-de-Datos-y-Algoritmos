import numpy as np


class ColadePrioridad:
    __array: np.array

    
    def __init__(self, dimension):
        self.__array = np.full(dimension, 0)
        self.__array[0] = 0
    
    def padre(self, pos):
        return pos // 2
    
    def hijo_izquierdo(self, pos):
        return 2 * pos
    
    def hijo_derecho(self, pos):
        return (2 * pos) + 1
    
    def esHoja(self, pos):
        return pos*2 > len(self.__array)
    
    def intercambio(self, pos1, pos2):
        self.__array[pos1], self.__array[pos2] = self.__array[pos2], self.__array[pos1]
    
    def Vacio(self):
        return self.__array[0] == 0

    
    def Lleno(self):
        return self.__array[0] == len(self.__array)

    
    def insertar(self, element):
        if self.Lleno():
            return print("No hay espacio en la cola")
        else:
            self.__array[0] += 1
            actual = self.__array[0]
            self.__array[actual] = element
            
            while self.__array[actual] < self.__array[self.padre(actual)]:
                self.intercambio(actual, self.padre(actual))
                actual = self.padre(actual)
    
    
    def mostrar(self):
        for i in range(1,(self.__array[0] // 2+1)):
            print(" PADRE : "+ str(self.__array[i])+" HIJO IZQUIERDO : "+ 
                                str(self.__array[2 * i])+" HIJO DERECHO: "+
                                str(self.__array[(2 * i) + 1]))