from Simulacion import Simulacion

if __name__=="__main__":
    frecuencia=int(input("Ingrese el tiempo de frecuencia de llegada de los clientes:"))
    tSimulacion=int(input("Ingrese el tiempo de simulacion:"))
    tCajero=int(input("Ingrese el tiempo de cajero:"))

    simulacion = Simulacion(tSimulacion,frecuencia,tCajero)
    simulacion.ejecutar()