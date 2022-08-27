import imp
from ColaEncadenada import ColaEncadenada

class Simulacion():
    __tTranscurrido:int
    __tSimulacion:int
    __tFrecuenciaCliente:int
    __tFrecuenciaCaja:int
    __tTotal:int
    __clientesTotales:int
    __clientesAtendidos:int
    __colaCaja=None

    def __init__(self,tsimulacion,tfrecuencia,tcajero) -> None:
        self.__tSimulacion = tsimulacion
        self.__tFrecuenciaCliente = tfrecuencia
        self.__tFrecuenciaCaja = tcajero
        self.__tTranscurrido = 0
        self.__tTotal = 0
        self.__clientesAtendidos = 0
        self.__clientesTotales = 0
        self._colaCaja=ColaEncadenada()
    

    def ejecutar(self):
        while self.__tSimulacion > self.__tTranscurrido:

            self.__tTotal += self._colaCaja.getlongitud()

            if self.__tTranscurrido % self.__tFrecuenciaCliente == 0 and self.__tTranscurrido != 0:
                self._colaCaja.insertar("cliente")
                self.__tTotal+= self.__tFrecuenciaCaja - self.__tFrecuenciaCliente
                self.__clientesTotales += 1
            if (self.__tTranscurrido - self.__tFrecuenciaCliente) % self.__tFrecuenciaCaja == 0 and self.__tTranscurrido != 2:
                self.__clientesAtendidos += 1
                self._colaCaja.suprimir()
            
            self.__tTranscurrido += 1
        self.__tTotal-=self.__tFrecuenciaCliente
        print("----------------------------------")
        print("La cantidad de clientes Atendidos es: {}".format(self.__clientesAtendidos))
        print("La cantidad de clientes Totales es: {}".format(self.__clientesTotales))
        print("El Tiempo promedio de espera del cliente es : {:.2f}".format(self.__tTotal/self.__clientesTotales))