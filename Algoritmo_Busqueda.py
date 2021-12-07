from Nodo import Nodo
from Espacio_Estados import Espacio_Estados
from Estado import Estado 
from Frontera import Frontera

import Variables

class Algoritmo_Busqueda:

    def __init__(self):
        self.initState = Variables.initState
        self.bottleSize = Variables.bottleSize
        self.camino = []
        self.visitados = set()
        self.frontera = Frontera()


    def algoritmoBusqueda(self):
        id = 0
        estado = Estado(self.initState).getEstado()
        padre = None
        accion = None
        nodo = Nodo(id, estado, padre, accion)       
        espacio_estados = Espacio_Estados()
        self.frontera.insertarNodo(nodo)
        solucion = False
        while self.frontera.estaVacia() == False and solucion == False:
            nodo = self.frontera.sacarNodo()
            solucion = espacio_estados.objetivo(nodo.getEstado())
            if solucion:
                break

            elif nodo.getMd5estado() not in self.visitados and nodo.getProfundidad() < Variables.profundidad:
                self.visitados.add(nodo.getMd5estado())
                espacio_estados.obtenerSucesores(nodo.getEstado())
                lista_sucesores= espacio_estados.getSucesores()
                for i in range(len(lista_sucesores)):
                    id += 1
                    accion, estado = lista_sucesores[i]
                    nodo_hijo = Nodo(id, estado, nodo, accion)
                    self.frontera.insertarNodo(nodo_hijo)

        if solucion:
            self.generarCamino(nodo)
 

    def generarCamino(self, nodo):
        while nodo.getPadre() is not None:
            self.camino.append(nodo)
            nodo = nodo.getPadre()

        self.camino.append(nodo)
        self.camino.reverse()

        file = open("{0}_{1}.txt".format(Variables.id_problema, Variables.nombre_estrategia), "w+") 
        for i in range(0, len(self.camino)):
            file.write("\n" + self.camino[i].toString())
        file.close


    def getCamino(self):
        return self.camino

    
    def getVisitados(self):
        return self.visitados
