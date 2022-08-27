import numpy as np


class PilaSecuencial:
    __array = None
    __tope1 = None
    __tope2 = None
    __cantidadmax = None

    def __init__(self, dimension):
        self.__cantidad = 0
        self.__tope1= 0
        self.__tope2 = dimension - 1
        #self.__items = []  CON LISTAS
        self.__cantidadmax = dimension
        self.__array = np.empty(dimension, dtype=int)

    def insertar(self, elemento):
        pila = int(input("Ingrese la pila que desea utilizar para ingresar( 1 / 2)"))
        if self.pilaLlena():
            if pila == 1:
                self.__array[self.__tope1]=elemento
                print(self.__array[self.__tope1])
                self.__tope1 += 1
            elif pila == 2:
                self.__array[self.__tope2]=elemento
                print(self.__array[self.__tope2])
                self.__tope2 -= 1
            else:
                print("La pila ingresada no existe")
        else:
            print("No se puede agregar La pila esta llena")

    def suprimir(self):
        pila = int(input("Ingrese la pila que desea utilizar para eliminar( 1 / 2)"))
        if pila == 1 and self.vaciaPila1():
            np.delete(self.__array, self.__tope1)
            self.__tope1 -= 1
        elif pila == 2 and self.vaciaPila2():
            np.delete(self.__array, self.__tope2)
            self.__tope2 += 1
        else:
            print("La pila ingresada no existe")

    def recorrer(self):
        print("Elementos de la pila: 1")
        while self.__tope1 > 0:
            #self.suprimir()
            self.__tope1 -= 1
            print(self.__array[self.__tope1])

        print("Elementos de la pila: 2")
        while self.__tope2 < self.__cantidad-1:
            #self.suprimir()
            self.__tope2 += 1
            print(self.__array[self.__tope2])

    def vaciaPila1(self):
        x = False
        if self.__cantidadmax != 0:
            x = True
        return x

    def vaciaPila2(self):
        x = False
        if self.__cantidadmax != 0:
            x = True
        return x

    def pilaLlena(self):
        x = False
        if self.__tope1 + 1 < self.__tope2:
            x = True
        return x