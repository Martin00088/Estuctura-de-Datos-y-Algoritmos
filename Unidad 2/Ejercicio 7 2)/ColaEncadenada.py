from Nodo import Nodo


class ColaEncadenada():
    __ultimo:Nodo
    __primero:Nodo
    __cantidad = None

    def __init__(self) -> None:
        self.__ultimo = None
        self.__primero = None
        self.__cantidad = 0 

    def mostrar(self) -> str:
        aux = self.__primero 
        while aux is not None:            
            print(aux.getDato())
            aux=aux.getSiguiente()

    def insertar(self,elemento):
        nuevo=Nodo(elemento)
        if self.__ultimo == None:
            self.__primero=nuevo
        else:
            self.__ultimo.setSiguiente(nuevo)
        self.__cantidad += 1
        self.__ultimo = nuevo  

    def Vacia(self):
        return self.__cantidad == 0

    def suprimir(self):
        if self.Vacia():
            print("La cola esta vacia no se puede eliminar")
        else:
            aux= self.__primero
            self.__primero = aux.getSiguiente()
            del aux
            self.__cantidad -= 1

    def getlongitud(self):
        return self.__cantidad