### DH0001 Estratificación Univaria D&H
#### Descripción.
Cargaremos la capa y abriremos las propiedades para modificar la simbologia. Se espera obtener como resultados una nueva columna con un número identificador para el estrato que le corresponde a cada variable ya clasificada.


#### Prerrequisitos.
+ gvSIG desktop 2.4.0.
+ Vista nueva y cargar el archivo [Censo_Eco_Estatal.csv](https://github.com/Arturo-GoGa/EstratificacionDaleniusHodges/blob/main/data/Censo_Eco_Estatal.csv)
+ Acceso a tabla de atributos y activa.


#### Pasos.
1. Cargar la capa ``Censo_Eco_Estatal.csv`` a la vista.
2. Daremos click derecho sobre la vista activa y seleccionaremos la opcion de ``propiedades``.
3. Pasaremos a la pestaña de ``Simbologia`` y desplegaremos el apartado de ``Cantidades``.
4. En el desplegable seleccionaremos ``Intervalos``, del lado derecho desplegamos la barra de "Tipo de Intervalo" y seleccionamos ``Dalenius & Hodges``.
5. A continuacion introduciremos el numero ``4`` en el recuadro de "N° de Intervalos y daremos click en la parte de abajo en ``Calcular Intervalos``.
6. Seleccionaremos los colores para cada intervalo dando doble click sobre el color cargado por defecto, despues sobre el boton ``Seleccionar Simbolo`` y click sobre el boton con el simbolo de ``...``  en la opcion de "Color de Relleno", y escogemos la pestaña de "RGB" y introduciremos los codigos para cada intervalos , primer intervalo: ``E61900``, Segundo Intervalo: ``CC0000``, Tercer Intervalo: ``991919`` y Cuarto Intervalo: ``660000``.
7. Daremos click en ``Aplicar`` y ``Aceptar"


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
