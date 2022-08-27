import numpy as np


class PilaSecuencial:
    __items = None
    __tope = None
    __cantidad = None

    def __init__(self, dimension):
        self.__cantidad = 0
        self.__tope = -1
        #self.__items = []  CON LISTAS
        self.__items = np.empty(dimension, dtype=int)

    def insertar(self, elemento):
        print(elemento)
        if self.__tope < self.__cantidad:
            self.__tope += 1
            #self.__items = np.append(self.__items[self.__tope], elemento)
            self.__items[self.__tope]=elemento
            print("{}".format(self.__items[self.__tope]))
            self.__cantidad += 1
        else:
            print("No se puede agregar La pila esta llena")

    def suprimir(self):
        if self.__tope == -1:
            print("La pila esta vacia")
        else:
            #self.__items.pop(self.__tope) CON LISTA
            self.__items=np.delete(self.__items, self.__tope)
            self.__tope -= 1
            self.__cantidad -= 1

    def mostrar(self):
        for i in range(self.__cantidad):
            print("El elemento numero {} en la pila es {}".format(i+1, self.__items[i]))

    def vacia(self):
        x = False
        if self.__cantidad != 0:
            x = True
        return x
