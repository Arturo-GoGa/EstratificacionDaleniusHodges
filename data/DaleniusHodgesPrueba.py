# encoding: utf-8

# Estratificacion Dalenius and Hodges

from gvsig import *
from gvsig.commonsdialog import *
from gvsig.libs.toolbox import *
from es.unex.sextante.gui import core
from es.unex.sextante.gui.core import NameAndIcon
from org.gvsig.geoprocess.lib.api import GeoProcessLocator
import math

class EstraDH(ToolboxProcess):
    def defineCharacteristics(self):
        self.setName ("Estratificacion Dalenius & Hodges")
        self.setGroup("Vectorial")
        params = self.getParameters()
        params.addInputVectorLayer("LAYER", "Capa de Entrada", SHAPE_TYPE_POLYGON, True)
        params.addNumericalValue("E", "Estratos", 0, NUMERICAL_VALUE_INTEGER)
        params.addInputTable("TABLE", "Tabla de Contenido", True)
        params.addTableField("VARIABLE", "Variable", "TABLE", True)
        self.addOutputVectorLayer("RESULTADO", "Estratificado", SHAPE_TYPE_POLYGON)

    def processAlgorithm(self):
        features = None
        try:
        
            params = self.getParameters()
            layer = params.getParameterValueAsVectorLayer("LAYER")
            e = params.getParameterValueAsInteger("E")
            table = params.getParameterValueAsTable("TABLE")
            field = params.getParameterValueAsInt("VARIABLE")
            
            input_store = layer.getFeatureStore()
            features = input_store.getFeatureSet()
            
            output_store = self.builOutPutStore(
                features.getDefaultFeatureType(),
                SHAPE_TYPE_POLYGON,
                "EstraDH_FINAL",
                "RESULTADO"
                )


            #----- Paso 2 Orden ascendente
            dato_orden = [] 
            for y in range (len(field)):
              dato_orden.append(field[y])
            dato_orden.sort()
        
        
            #----- Paso 3  Rango
            j=((e*10 +len(field))-(abs(len(field)-e*10)))/2
            rango = (float(dato_orden[-1]) - float(dato_orden[0]))/j # tranformamos los datos de entrada para 
                                      # que sea en decimal.
    
                                   
            #----- Paso 4 limites minimos y maximos. 
            lim_min = [] 
            lim_max = []
            lim_min.append (dato_orden[0])
            for i in range (len(field)):
               lim_max.append(lim_min[i] + rango)
               lim_min.append(lim_max[i])
            lim_min=lim_min[0:-1] #eliminamos el ultimo dato por que esta de mas 
        
            #----- Paso 5 Frecuencia
            frecuencia = []
            fre = 0
            for h in range (0, len(field)):
               for k in range (0, len(field)):
                   if (dato_orden[k]>= lim_min[h] and dato_orden[k]< lim_max[h]): #solo se aplica el < para que 
                                              #se cuente en dos intervalos.
                       fre = fre + 1
               frecuencia.append(fre)
               fre = 0
            frecuencia[-1]=frecuencia[-1]+1 #Agregamos el ultimo valor maximo de manera manual.
          
          
            #----- Paso 6 Raiz Cuadrada
            raiz = []
            ra = []
            aux_raz = 0
            for t in range (0, len(field)):
                ra.append(math.sqrt(frecuencia[t]))
                aux_raz = aux_raz + ra [t] #calculamos la raiz acumulada.
                raiz.append(aux_raz)
        
            #----- Paso 7  Q
            q = []
            for r in range (1, e):
                q.append(((raiz [-1])/e)*r) 
        
            #----- Paso8 intervalos maximos y minimos. 
            inter_min = []
            inter_max = []
            ter = 0
            inter_min.append(dato_orden[0])
            for u in range (0, e-1):
                for w in range (0, len(field)):
                    if (q[u]<=raiz[w]): #se calcula la diferencia entre las distancias de las raices con q 
                                        #para que lija el valor del limite maximo de la que tenga menor diferencia
                                        
                        dif1=q[u]-raiz[w-1]
                        dif2=raiz[w]-q[u]
                        if dif1<dif2:
                          ter = (lim_max [w-1])
                        else:
                          ter = (lim_max [w]) 
                        break 
                inter_max.append(ter)
                inter_min.append(inter_max[u])
            inter_max.append(dato_orden[-1])
        
        
            #----- Paso 9 Asignacion de grado
            clasi = []
            num = len(inter_min) #longitud del bucle
            for i in range (0,len(field)):
                for j in range (num):
                    if (field[i] >= inter_min[j] and field[i] < inter_max[j]):
                        clasi.append(j+1)
                    elif (field[i]==inter_max[-1]): # se utiliza para agregar el ultimo dato.
                        clasi.append(num)
                        break

            newfeature = self.createNewFeature(output_store, feature)
            for i in range(len(features)):
                newfeature.set("D/H",clasi[i])
            output_store.insert(newfeature)
            output_store.finishEditing()
            
        finally:
            DisposeUtils.disposeQuietly(features)
            print "Proceso Terminado %s" % self.getCommandLineName()
            return True

def main(*args):

    process = EstraDH()
    process.selfregister("Scripting")
    gm = GeoProcessLocator.getGeoProcessManager()
    alg = gm.getAlgorithms()
    for a in alg:
        print a 
    process.updateToolbox()
    msgbox("Script incorporado %s, %s" % (process.getGroup(), process.getName()))
    
      
