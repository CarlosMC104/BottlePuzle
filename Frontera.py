class Frontera:

    def __init__(self):
        self.listaFrontera = []

    def insertarNodo(self, nodo):
        self.listaFrontera.append(nodo)
        self.listaFrontera.sort(key=lambda nodo: (nodo.getValor(),nodo.getIdNodo()))

    def sacarNodo(self):
        return self.listaFrontera.pop(0)

    def estaVacia(self):
        return self.listaFrontera == []

    def getFrontera(self):
        return self.listaFrontera
