from copy import deepcopy
import Variables

class Espacio_Estados:

    def __init__(self):
        self.lista_sucesores= []


    def obtenerSucesores(self,estado):
        self.lista_sucesores.clear()
        for i in range(len(estado)):
            for j in range(len(estado)):
                if len(estado[i])!=0 and i!=j:
                    accion=(i,j,estado[i][0][1])
                    posible=self.EsAccionPosible(estado,accion)
                    if posible:
                        nuevo_estado = self.Accion(estado, accion)
                        if(nuevo_estado!=None):
                            sucesor = (accion, nuevo_estado)
                            self.lista_sucesores.append(sucesor)
                            self.ordenarListaSucesores()
        
    
    def getSucesores(self):
        return self.lista_sucesores


    def ordenarListaSucesores(self):
        for j in range(len(self.lista_sucesores)-1):
            for i in range(len(self.lista_sucesores)-1):
                sucesor_i=self.lista_sucesores[i]
                sucesor_i1=self.lista_sucesores[i+1]
                accioni,estadoi,= sucesor_i
                accioni1,estadoi1 = sucesor_i1
                id_botella_origen_i,id_botella_destino_i,cantidad_i = accioni
                id_botella_origen_i1,id_botella_destino_i1,cantidad_i1 = accioni1
                if(id_botella_origen_i>id_botella_origen_i1):
                    self.lista_sucesores[i]=sucesor_i1
                    self.lista_sucesores[i+1]= sucesor_i
                elif (id_botella_origen_i==id_botella_origen_i1):
                    if (id_botella_destino_i>id_botella_destino_i1):
                        self.lista_sucesores[i]=sucesor_i1
                        self.lista_sucesores[i+1]= sucesor_i
                    elif (id_botella_destino_i==id_botella_destino_i1):
                        if (cantidad_i>cantidad_i1):
                            self.lista_sucesores[i]=sucesor_i1
                            self.lista_sucesores[i+1]= sucesor_i
    

    def EsAccionPosible(self,estado,accion):
        botella_origen, botella_destino, cantidad = accion
        es_posible = True
        cantidad_origen = 0
        cantidad_destino = 0
        if botella_origen != botella_destino:
            if len(estado[botella_destino])==0 or estado[botella_origen][0][0]==estado[botella_destino][0][0]:
                for i in range(len(estado[botella_origen])):
                        cantidad_origen += estado[botella_origen][i][1]
                for j in range(len(estado[botella_destino])):
                        cantidad_destino += estado[botella_destino][j][1]
                if (cantidad_origen-cantidad)>=0:
                    if (cantidad+cantidad_destino)>Variables.bottleSize:
                        es_posible=False
                else: es_posible=False
            else: 
                es_posible=False 
        else: es_posible=False	
        return es_posible


    def Accion(self,estado,accion):
        botella_origen, botella_destino, cantidad = accion
        cantidad_origen = estado[botella_origen][0][1]
        nuevo_estado = deepcopy(estado)
        if len(nuevo_estado[botella_destino])!=0:
            cantidad_destino = nuevo_estado[botella_destino][0][1]
            cantidad_total = cantidad_origen + cantidad_destino
            nuevo_estado[botella_destino][0]=[nuevo_estado[botella_origen][0][0],cantidad_total]
            nuevo_estado[botella_origen].pop(0)	
        else: nuevo_estado[botella_destino].insert(0, nuevo_estado[botella_origen].pop(0))
        return nuevo_estado

    
    def objetivo(self,estado): 
        objetivo = True
        
        for i in range(len(estado)):
            botella_analizar = estado[i]
            cantidad_color=0
            if(len(botella_analizar)!=0):
                color_analizar = botella_analizar[0][0]
                for j in range(len(botella_analizar)):
                    cantidad_color= cantidad_color + botella_analizar[j][1]
                    if color_analizar != botella_analizar[j][0]: 
                        objetivo = False 
                        break
                    if cantidad_color!= Variables.bottleSize:
                        objetivo=False
                        break

        return objetivo