from MonticuloBinario import ColadePrioridad

if __name__ == "__main__":
    monticulo = ColadePrioridad(8)
    monticulo.insertar(4)
    monticulo.insertar(3)
    monticulo.insertar(22)
    monticulo.insertar(8)
    monticulo.insertar(10)
    monticulo.insertar(20)
    monticulo.insertar(60)
    monticulo.mostrar()
