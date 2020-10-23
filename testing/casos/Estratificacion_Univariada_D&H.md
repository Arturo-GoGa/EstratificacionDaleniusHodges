### DH0001 Estratificación Univaria D&H
##### Descripción.
Cargar la tabla de atributos de la capa y realizar los cálculos correspondientes para la estratificación y crear una nueva columna con los estratos correspondientes a cada variable.


##### Prerrequisitos.
+ gvSIG desktop 2.4.0.
+ Vista nueva y cargada un archivo dHP  -- definir un archivo con el nombre 
+ Acceso a tabla de atributos.


##### Pasos.
1. Cargar capa SHP a la vista.
2. Mostrar tabla de atributos.
3. Seleccionar la columna con la que se va a trabajar (numérica).
4. Ordenar los datos de manera Ascendente.
5. Hacer el conteo de todos los casos.
6. Calcular el logaritmo del total de los Casos.
7. Calculamos el los intervalos adecuados con la fórmula '1+(3.3*LOG(n))'.
8. Calcular el rango del indice restando el valor mayor menos el menos.
9. Calcular los intervalos de construcción para `n` dividiendo el rango del indice entre los intervalos adecuados.
10. Construir los limites de rangos, se tomara el valor pequeño de las variables como limite mínimo y se le sumara el intervalo de construcción para tomar él limite máximo, se tomara este ultimo limite máximo como él limite mínimo del siguiente rango.
11. Calcular la frecuencia de cada límite de rango.
12. Calcular la raíz cuadrada de cada frecuencia.
13. Calcular la raíz cuadrada acumulada con la raíz de las frecuencias.
14. Calcular los estratos con dividiendo el total de la raíz acumulada de las frecuencias entre los estratos, el resultado sera el estrato 1 y se sumara ese mismo resultados la cantidad para cada estrato.
15. Calcular la distancia entre cada estrato y cada frecuencia acumulada, se toma como valor fijo el valor del estrato y se va restando cada una de las raíces acumuladas de las frecuencias.
16. Para definir los grados se tomara la distancia entre los estratos y las raíces y cuando este sea cero con décimas se tomara como él limite del estrato.
17. Asignar a cada uno de los grados un numero identificador.
18. Crear una nueva columna en la tabla de atributos clasificando el valor de la variable a cada uno de los grados y colocando el identificador. 


##### Resultados Esperados.
Se espera obtener como resultados una nueva columna con un número identificador para el estrato que le corresponde a cada variable ya clasificada.
--intervalos 

##### Reportar Fallo.
