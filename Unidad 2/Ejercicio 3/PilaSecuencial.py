import numpy as np


class PilaSecuencial:
    __array = None
    __tope = None
    __cantidad = None

    def __init__(self, dimension):
        self.__cantidad = 0
        self.__tope = -1
        #self.__items = []  CON LISTAS
        self.__array = np.empty(dimension, dtype=int)

    def insertar(self, elemento):
        if self.__tope < self.__cantidad:
            self.__tope += 1
            #self.__items = np.append(self.__items[self.__tope], elemento)
            self.__array[self.__tope]=elemento
            self.__cantidad += 1
        else:
            print("No se puede agregar La pila esta llena")

    def suprimir(self):
        if self.__tope == -1:
            print("La pila esta vacia")
        else:
            #self.__items.pop(self.__tope) CON LISTA
            self.__array = np.delete(self.__array, self.__tope)
            self.__tope -= 1
            self.__cantidad -= 1

    def mostrar(self):
        tot = 1
        while self.__tope > 0:
            self.suprimir()
            tot *= self.__array[self.__tope]
        print("El numero Factorial es {}".format(tot))

    def vacia(self):
        x = False
        if self.__cantidad != 0:
            x = True
        return x

    def Factorial(self, numero):
        while int(numero) > 0:
            self.insertar(numero)
            numero = numero - 1
