class Celda:
    __item = None
    __celdasig = None

    def getItem(self):
        return self.__item

    def setItem(self, item):
        self.__item=item

    def setSiguiente(self, siguiente):
        self.__celdasig = siguiente

    def getSiguiente(self):
        return self.__celdasig
