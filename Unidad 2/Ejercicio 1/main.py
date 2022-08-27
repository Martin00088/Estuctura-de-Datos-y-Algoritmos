from PilaEncadenada import PilaEncadenada
from PilaSecuencial import PilaSecuencial

if __name__=="__main__":

    #PILA SECUENCIAL
    pSecuencial=PilaSecuencial(5)
    print(pSecuencial.vacia())
    pSecuencial.insertar(1)
    pSecuencial.insertar(2)
    pSecuencial.insertar(3)
    pSecuencial.mostrar()
    print("--------Suprime------------------")
    pSecuencial.suprimir()
    pSecuencial.mostrar()
    print(pSecuencial.vacia())
    print("--------------------------")

    #PILA ENCADENADA
    pEncadenada=PilaEncadenada()
    print(pEncadenada.vacia())
    pEncadenada.insertar("Auto")
    pEncadenada.insertar("Moto")
    pEncadenada.insertar("Camion")
    pEncadenada.mostrar()
    pEncadenada.suprimir()
    pEncadenada.mostrar()
