import json
import sys
import Variables
class LeerProblema:
    
    def __init__(self):
        pass

    def consistenciaJson():
        try:
            archivo = open('problema.json').read()
            problema = json.loads(archivo)
        except FileNotFoundError:
            print ("ERROR. Archivo'{0}'no encontrado".formato(jsonFile))
            sys.exit(0)
        except UnicodeDecodeError:
            print ("ERROR. Por favor, inserta un archivo .json")
            sys.exit(0)
        except:
            print("Json inconsistente. Error sintáctico")
            sys.exit(0)

        consistencia= True
        estado_inicial= problema['initState']
        bottleSize = problema['bottleSize']
        for i in range(len(estado_inicial)):
            if(len(estado_inicial[i]))!=0:
                color=estado_inicial[i][0][0]
                cantidad_botellas=0
                for j in range(len(estado_inicial[i])):

                    if isinstance(estado_inicial[i][j][1], int)==False or isinstance(estado_inicial[i][j][0], int)==False or estado_inicial[i][j][1]<=0:
                        consistencia=False
                        print("Json inconsistente. Hay botellas con cantidades erroneas o datos no válidos")
                        sys.exit(0)

                    cantidad_botellas = cantidad_botellas + estado_inicial[i][j][1]

                    if cantidad_botellas > bottleSize:
                        consistencia=False
                        print("Json inconsistente. Alguna botella tiene mas cantidad de la permitida")
                        sys.exit(0)
                    
                    if estado_inicial[i][j][0] != color or j==0:
                        color = estado_inicial[i][j][0]
                    else:
                        consistencia = False
                        print("Json inconsistente. Hay colores que se muestran como cantidades separadas siendo el mismo color")
                        sys.exit(0) 
        return problema


    def obtenerProblema(problema):
        id = problema['id']
        BottleSize = problema['bottleSize']
        estado_inicial = problema['initState']

        Variables.id_problema = id
        Variables.bottleSize = BottleSize
        Variables.initState = estado_inicial

