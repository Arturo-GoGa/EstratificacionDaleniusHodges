### DH0001 Estratificación Univaria D&H
#### Descripción.
Cargar la tabla de atributos de la capa y realizar los cálculos correspondientes para la estratificación y crear una nueva columna con los estratos correspondientes a cada variable. Se espera obtener como resultados una nueva columna con un número identificador para el estrato que le corresponde a cada variable ya clasificada.


#### Prerrequisitos.
+ gvSIG desktop 2.4.0.
+ Vista nueva y cargada la capa "AGE_Estatales.shp"
+ Acceso a tabla de atributos.


#### Pasos.
1. Cargar la capa ``AGE_estatales.shp`` a la vista.
2. Mostrar tabla de atributos.
3. Seleccionar la columna ``CECO_001``.
4. Ordenar los datos de manera ascendente.
5. Hacer el conteo de todos los casos.
6. Calcular el logaritmo del total de los Casos.
7. Calculamos los intervalos adecuados con la fórmula `1+(3.3*LOG(n))`.
8. Calcular el rango del indice restando el valor mayor menos el menos.
9. Calcular los intervalos de construcción para `n` dividiendo el rango del indice entre los intervalos adecuados.
10. Construir los limites de rangos, se tomara el valor pequeño de las variables como limite mínimo y se le sumara el intervalo de construcción para tomar él limite máximo, se tomara este ultimo limite máximo como él limite mínimo del siguiente rango (se le puede sumar ``0.000001`` para que no sea totalmente identico).
11. Calcular la frecuencia de cada límite de rango.
12. Calcular la raíz cuadrada de cada frecuencia.
13. Calcular la raíz cuadrada acumulada con la raíz de las frecuencias.
14. Calcular los estratos con dividiendo el total de la raíz acumulada de las frecuencias entre los estratos, el resultado sera el estrato 1 y se sumara ese mismo resultados la cantidad para cada estrato.
15. Calcular la distancia entre cada estrato y cada frecuencia acumulada, se toma como valor fijo el valor del estrato y se va restando cada una de las raíces acumuladas de las frecuencias.
16. Para definir los grados se tomara la distancia entre los estratos y las raíces y cuando este sea cero con décimas se tomara como él limite del estrato.
17. Se asignara un numero a cada grado como identificador empezando con el numero ``1`` para el grado mas pequeño y asi sucesivamente.
18. se crea una nueva columna en la tabla de atributos clasificando el valor de la variable a cada uno de los grados y colocando el identificador. 


#### Resultados Esperados.

CVE_ENT: Clave de entidad federativa. 
CECO_001: identificador para la ``Poblacion economicamente activa``
Identificador: resultante del metodo Dalenius&Hodges

|Identificador | Grado|
|:------------:|------|
| 1| Bajo |
| 2| Medio Bajo|
| 3| Medio Alto|
| 4| Alto |

##### Resultados en la tabla 
|CVE_ENT	|  CECO_001  |	Identificador| 
|:--------|:------------|:--------:|
|01	|540692|	1|
|02	|1463802|	2|
|03	|326564|	1|
|04	|363555|	1|
|05	|1182013|	1|
|06	|319574|	1|
|07	|1698428|	2|
|08	|1427766|	2|
|09	|4205072|	4|
|10	|615419| 1|
|11	|2257943|	2|
|12	|1182214|	1|
|13	|1048451|	1|
|14	|3256882|	3|
|15	|6507365|	4|
|16	|1699569|	2|
|17	|802856|	1|
|18	|467031|	1|
|19	|2150819|	2|
|20	|1283262|	1|
|21	|2267222|	2|
|22	|863776|	1|
|23	|690682|	1|
|24	|987058|	1|
|25	|1162695|	1|
|26	|1178848|	1|
|27	|861144|	1|
|28	|1355011|	2|
|29	|495846|	1|
|30	|2956089|	3|
|31	|868376|	1|
|32	|506456|	1|

#### Reportar Fallo. 


