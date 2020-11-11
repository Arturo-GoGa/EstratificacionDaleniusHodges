### DH0001 Estratificación Univaria D&H
#### Descripción.
Cargaremos la capa y abriremos las propiedades para modificar la simbologia. 


#### Prerrequisitos.
+ gvSIG desktop 2.4.0.
+ Vista nueva y cargar el archivo [Censo_Eco_Estatal.csv](https://github.com/Arturo-GoGa/EstratificacionDaleniusHodges/blob/main/data/Censo_Eco_Estatal.csv)
+ Acceso a tabla de atributos y activa.


#### Pasos.
1. Cargar la capa ``Censo_Eco_Estatal.csv`` a la vista.
2. Daremos click derecho sobre la vista activa y seleccionaremos la opcion de ``propiedades``.
3. Pasaremos a la pestaña de ``Simbologia`` y desplegaremos el apartado de ``Cantidades``.
4. En el desplegable seleccionaremos ``Intervalos``, del lado derecho desplegamos la barra de "Tipo de Intervalo" y seleccionamos ``Dalenius & Hodges``.
5. A continuacion introduciremos el numero ``4`` en el recuadro de "N° de Intervalos" y daremos click en la parte de abajo en ``Calcular Intervalos``.
6. Seleccionaremos los colores para cada intervalo dando doble click sobre el color cargado por defecto, despues sobre el boton ``Seleccionar Simbolo`` y click sobre el boton con el simbolo de ``...``  en la opcion de "Color de Relleno", y escogemos la pestaña de "RGB" y introduciremos los codigos para cada intervalos , primer intervalo: ``E61900``, Segundo Intervalo: ``CC0000``, Tercer Intervalo: ``991919`` y Cuarto Intervalo: ``660000``.
7. Daremos click en ``Aplicar`` y ``Aceptar".


#### Resultados Esperados.
Generara un Mapa como el Siguiente.

![Mapa](https://github.com/Arturo-GoGa/IMAGENES/blob/main/Mapa_CECO.PNG)

#### Reportar Fallo. 
