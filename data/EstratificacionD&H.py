# encoding: utf-8

# Estratificacion Dalenius and Hodges

import gvsig
import math 


def main(*args):


    #----- Paso0 Datos iniciales
    estratos=4 #Numero de estratos deseados

    #----- Paso1 Obtencion de datos
    sourceLayer = gvsig.currentLayer() #accede a la capa activa
    sourceStore = sourceLayer.getFeatureStore() #acceso al store de la capa
    sourceFeatures = sourceStore.getFeatures() #obtenemos los datos
    dato = []# datos desordenados 
    dato_orden = [] #datos ordenados ascendentemente 

    for fs in sourceFeatures:
        var = fs.get("CECO_001")#obtiene los valores de la tabla 
        dato.append(var)


    #----- Paso 2 Orden ascendente 
    for y in range (len(dato)):
      dato_orden.append(dato[y])
    dato_orden.sort()


    #----- Paso 3  Rango
    j=((estratos*10 +len(dato))-(abs(len(dato)-estratos*10)))/2
    rango = (float(dato_orden[-1]) - float(dato_orden[0]))/j # tranformamos los datos de entrada para 
															# que sea en decimal.
														
    #----- Paso 4 limites minimos y maximos. 
    lim_min = [] 
    lim_max = []
    lim_min.append (dato_orden[0])
    for i in range (len(dato)):
       lim_max.append(lim_min[i] + rango)
       lim_min.append(lim_max[i])
    lim_min=lim_min[0:-1] #eliminamos el ultimo dato por que esta de mas 

    #----- Paso 5 Frecuencia
    frecuencia = []
    fre = 0
    for h in range (0, len(dato)):
       for k in range (0, len(dato)):
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
    for t in range (0, len(dato)):
        ra.append(math.sqrt(frecuencia[t]))
        aux_raz = aux_raz + ra [t] #calculamos la raiz acumulada.
        raiz.append(aux_raz)

    #----- Paso 7  Q
    q = []
    for r in range (1, estratos):
        q.append(((raiz [-1])/estratos)*r) 

    #----- Paso8 intervalos maximos y minimos. 
    inter_min = []
    inter_max = []
    ter = 0
    inter_min.append(dato_orden[0])
    for e in range (0, estratos-1):
        for w in range (0, len(dato)):
            if (q[e]<=raiz[w]): #se calcula la diferencia entre las distancias de las raices con q 
                                #para que lija el valor del limite maximo de la que tenga menor diferencia
                                
                dif1=q[e]-raiz[w-1]
                dif2=raiz[w]-q[e]
                if dif1<dif2:
                  ter = (lim_max [w-1])
                else:
                  ter = (lim_max [w]) 
                break 
        inter_max.append(ter)
        inter_min.append(inter_max[e])
    inter_max.append(dato_orden[-1])


    #----- Paso 9 Asignacion de grado
    clasi = []
    num = len(inter_min) #longitud del bucle
    for i in range (0,len(dato)):
        for j in range (num):
            if (dato[i] >= inter_min[j] and dato[i] < inter_max[j]):
                clasi.append(j+1)
            elif (dato[i]==inter_max[-1]): # se utiliza para agregar el ultimo dato.
                clasi.append(num)
                break
  

    #----- Paso10 Ceación de nueva capa 
    sourceSchema=sourceLayer.getSchema() #Obtengo el esquema de la capa origen
    targetSchema=gvsig.createFeatureType(sourceSchema) #Creo/copio ese esquema, este será el de mi nueva capa
    targetSchema.append("D/H", "INTEGER", 10)# Añado al nuevo esquema el nuevo campo de tipo entero y tamaño 10
    targetLayer=gvsig.createShape(targetSchema, prefixname="AGE_Clasificada") #Creo una nueva capa con el nuevo esquema
    targetStore=targetLayer.getFeatureStore() #Obtengo el feature store de la nueva capa
    targetStore.edit() # Pongo en edición ese store
    for i in range(len(sourceFeatures)): #Recorro las features de la cap inicial
       newFeature=targetStore.createNewFeature(sourceFeatures[i]) #Creo nuevas features en el nuevo store a partir de las
                                                                  # features de la capa origen
       newFeature.set("D/H",clasi[i]) # A esas nuevas features les asigno la clasificación de Dalenius and Hodges
       targetStore.insert(newFeature) # Inserto las nuevas features en el store
    targetStore.finishEditing() # Una vez creadas y actualizadas las features termino edicion del store
    gvsig.currentView().addLayer(targetLayer) # Cargo la capa en la vista actual

