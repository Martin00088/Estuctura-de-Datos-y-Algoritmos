import numpy as np


class PilaSecuencial:
    __binario = None
    __tope = None
    __cantidad = None

    def __init__(self, dimension):
        self.__cantidad = 0
        self.__tope = -1
        #self.__items = []  CON LISTAS
        self.__binario = np.empty(dimension, dtype=int)

    def insertar(self, elemento):
        if self.__tope < self.__cantidad:
            self.__tope += 1
            #self.__items = np.append(self.__items[self.__tope], elemento)
            self.__binario[self.__tope]=elemento
            self.__cantidad += 1
        else:
            print("No se puede agregar La pila esta llena")

    def suprimir(self):
        if self.__tope == -1:
            print("La pila esta vacia")
        else:
            #self.__items.pop(self.__tope) CON LISTA
            np.delete(self.__binario, self.__tope)
            self.__tope -= 1
            self.__cantidad -= 1

    def mostrar(self):
        binario=""
        while self.__tope >= 0:
            binario += str(self.__binario[self.__tope])
            np.delete(self.__binario, self.__tope)
            self.__tope -= 1
        print("El numero binario es {}".format(binario))

    def vacia(self):
        x = False
        if self.__cantidad != 0:
            x = True
        return x

    def ConvDecABin(self, decimal):
        while int(decimal)/2 >= 1:
            binario = decimal % 2
            self.insertar(binario)
            decimal = int(decimal/2)
        self.insertar(int(decimal))
