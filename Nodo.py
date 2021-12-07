import Variables
import hashlib

class Nodo:

    def __init__(self, id, estado, padre, accion):
        self.id = id
        self.nodoPadre = padre
        self.estado = estado
        self.accion = accion
        self.heuristica = self.calcularHeuristica()
        self.md5estado = self.generarMd5()
       

        if self.nodoPadre is None:
            self.costo = 0.0
            self.profundidad = 0
        else:
            self.costo = padre.getCosto()+1.0
            self.profundidad = padre.getProfundidad() + 1
        self.valor = self.generarValor()
        self.valorTruncado = self.truncarValor()

      

    def getIdNodo(self):
        return self.id

    def getPadre(self):
        return self.nodoPadre

    def getIdPadre(self):
        if self.getPadre() is None:
            return None
        else:
            return self.getPadre().getIdNodo()

    def getAccion(self):
        if self.accion is None:
            return None
        else:
            return self.accion

    def getEstado(self):
        return self.estado

    def getHeuristica(self):
        return self.heuristica

    def getCosto(self):
        return self.costo

    def getProfundidad(self):
        return self.profundidad

    def getValor(self):
        return self.valor
    
    def getValorTruncado(self):
        return self.valorTruncado
    
    def getMd5estado(self):
        return self.md5estado


    def generarMd5(self):
        estado_md5 = str(self.estado)
        estado_md5 = estado_md5.replace(" ", "")
        estado_md5 = hashlib.md5(estado_md5.encode())
        estado_md5 = estado_md5.hexdigest()
        return estado_md5


    def generarValor(self):
        if Variables.nombre_estrategia == "DEPTH":  # Profundidad
            self.valor = 1/(self.profundidad+1)
        elif Variables.nombre_estrategia == "BREADTH":  # Anchura
            self.valor = self.profundidad
        elif Variables.nombre_estrategia == "UNIFORM":  # Costo uniforme
            self.valor = self.costo
        elif Variables.nombre_estrategia == "GREEDY":  # Voraz
            self.valor = self.heuristica
        else:   # A*
            self.valor = self.costo + self.heuristica
        return self.valor
    
    def truncarValor(self):
        self.valorTruncado = round(self.valor,2)
        return self.valorTruncado


    def calcularHeuristica(self):
        self.heuristica = 0.0
        lista_colores = []
        e = self.getEstado()
        for i in range(len(e)):
            if  not e[i]:
                self.heuristica += 1.0
                
            else:
                self.heuristica += len(e[i])
                if e[i][0][0] not in lista_colores:
                    lista_colores.append(e[i][0][0])
                else: self.heuristica = self.heuristica + 1

        self.heuristica = self.heuristica - len(e)               

        return self.heuristica

    def toString(self):
        return("[{0}][{1},{2},{3},{4},{5},{6},{7}]".format(self.getIdNodo(), self.getCosto(), self.getMd5estado(), self.getIdPadre(), self.getAccion(), self.getProfundidad(),self.getHeuristica(), self.getValorTruncado()))
