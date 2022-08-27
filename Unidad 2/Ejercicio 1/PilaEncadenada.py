from Celda import Celda


class PilaEncadenada:
    __cantidad = None
    __tope= -1

    def __init__(self):
        self.__cantidad = 0
        self.__tope = None

    def vacia(self):
        x=True
        if self.__cantidad != 0:
            x=False
        return x

    def insertar(self, elemento):
        newcelda = Celda()
        newcelda.setItem(elemento)
        newcelda.setSiguiente(self.__tope)
        self.__tope = newcelda
        self.__cantidad += 1
        print("Elemento Insertado con exito ({})".format(newcelda.getItem()))

    def suprimir(self):
        if self.vacia():
            print("No se puede suprimir porque la Pila esta vacia")
        else:
            aux = self.__tope
            self.__tope = self.__tope.getSiguiente()
            print("El elemento {} fue eliminado exitosamente".format(aux.getItem()))
            self.__cantidad -= 1

    def mostrar(self):
        aux = self.__tope
        while aux != None:
            print(aux.getItem())
            aux = aux.getSiguiente()

