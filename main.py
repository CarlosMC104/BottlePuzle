import json
import sys
import os
from LeerProblema import LeerProblema
from Estado import Estado
from Espacio_Estados import Espacio_Estados
from Nodo import Nodo
from Algoritmo_Busqueda import Algoritmo_Busqueda
import Variables


def elegirEstrategia():
        valido = False
        while valido==False:
            try:
                option = int(input(( "\nElige la estrategia [1, 2, 3, 4, 5]:\n\t1. Profundidad\n\t2. Anchura\n\t3. Costo Uniforme\n\t4. Voraz\n\t5. A*\n\n")))
                if 1 <= option <= 5:
                    valido = True
                    if option == 1: Variables.nombre_estrategia = "DEPTH"
                    elif option == 2: Variables.nombre_estrategia = "BREADTH"
                    elif option == 3: Variables.nombre_estrategia = "UNIFORM"
                    elif option == 4: Variables.nombre_estrategia = "GREEDY"
                    else: Variables.nombre_estrategia = "A"
                else:
                    print("Introduce un valor válido [1, 2, 3, 4, 5]\n")
            except ValueError:
                print("introduce un valor válido [1, 2, 3, 4, 5]\n")

			

def main():
    problema = LeerProblema.consistenciaJson()
    elegirEstrategia()
    LeerProblema.obtenerProblema(problema)
    busqueda = Algoritmo_Busqueda()
    busqueda.algoritmoBusqueda()
    print("Programa finalizado")
    print("-"*100)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("-"*100)
        print("Programa interrumpido.\n")
        sys.exit(0)
