### DH0001 Estratificación Univaria D&H
#### Descripción.
Cargaremos la capa y obtendremos la estratificacion Dalenius & Hodges.
Se espera obtener como resultados una nueva columna con un número identificador para el estrato que le corresponde a cada variable.


#### Prerrequisitos.
+ gvSIG desktop 2.4.0.
+ Vista nueva y cargada la capa [Censo_Pob_Mun_Edomex.csv](https://github.com/Arturo-GoGa/EstratificacionDaleniusHodges/)
+ Acceso a tabla de atributos.


#### Pasos.
1. Cargar la capa ``Censo_Pob_Mun_Edomex.csv`` a la vista.
2. Vamos a dar click en la pestaña ``Herramientas`` y a continuacion seleccionamos ``Geoprocesamientos".
3. Del desplegado seleccionamos ``Caja de Herramientas``, de la ventana que se abre buscaremos ``Capas Vectoriales`` y lo expandiremos.
4. Daremos doble click sobre ``Dalenius& Hodges`` y se abrira una ventana.
5. Sobre la ventana en la variable _"Capa de Entrada"_ escogeremos la capa ``Censo_Pob_Mun_Edomex.csv``, despues en _"Campo"_ Seleccionamos ``pobtot`` y por ultimo introduciremos en _"Estratos"_ el numero ``5``.
6. Daremos click en aceptar.
18. Se crea una nueva columna en la tabla de atributos colocando el identificador a cada caso. 


#### Resultados Esperados.

|	ClaveMun	|	Clasificación	|		ClaveMun	|	Clasificación	|		ClaveMun	|	Clasificación	|
|:--------|:------------|:--------|:------------|:--------|:------------|
|	15001	|	2	|	15043	|	1	|	15085	|	2	|
|	15002	|	3	|	15044	|	1	|	15086	|	1	|
|	15003	|	2	|	15045	|	3	|	15087	|	3	|
|	15004	|	1	|	15046	|	1	|	15088	|	3	|
|	15005	|	3	|	15047	|	2	|	15089	|	1	|
|	15006	|	1	|	15048	|	2	|	15090	|	2	|
|	15007	|	1	|	15049	|	1	|	15091	|	2	|
|	15008	|	1	|	15050	|	1	|	15092	|	2	|
|	15009	|	2	|	15051	|	3	|	15093	|	1	|
|	15010	|	1	|	15052	|	1	|	15094	|	1	|
|	15011	|	2	|	15053	|	2	|	15095	|	3	|
|	15012	|	1	|	15054	|	4	|	15096	|	1	|
|	15013	|	5	|	15055	|	1	|	15097	|	1	|
|	15014	|	3	|	15056	|	1	|	15098	|	1	|
|	15015	|	1	|	15057	|	5	|	15099	|	4	|
|	15016	|	1	|	15058	|	5	|	15100	|	1	|
|	15017	|	1	|	15059	|	1	|	15101	|	2	|
|	15018	|	2	|	15060	|	4	|	15102	|	1	|
|	15019	|	1	|	15061	|	1	|	15103	|	2	|
|	15020	|	4	|	15062	|	2	|	15104	|	5	|
|	15021	|	1	|	15063	|	1	|	15105	|	1	|
|	15022	|	1	|	15064	|	1	|	15106	|	5	|
|	15023	|	1	|	15065	|	1	|	15107	|	1	|
|	15024	|	3	|	15066	|	1	|	15108	|	3	|
|	15025	|	4	|	15067	|	2	|	15109	|	5	|
|	15026	|	1	|	15068	|	1	|	15110	|	2	|
|	15027	|	1	|	15069	|	1	|	15111	|	2	|
|	15028	|	1	|	15070	|	4	|	15112	|	2	|
|	15029	|	4	|	15071	|	1	|	15113	|	2	|
|	15030	|	1	|	15072	|	1	|	15114	|	3	|
|	15031	|	5	|	15073	|	1	|	15115	|	2	|
|	15032	|	1	|	15074	|	3	|	15116	|	1	|
|	15033	|	5	|	15075	|	1	|	15117	|	1	|
|	15034	|	1	|	15076	|	2	|	15118	|	4	|
|	15035	|	3	|	15077	|	1	|	15119	|	1	|
|	15036	|	1	|	15078	|	1	|	15120	|	3	|
|	15037	|	4	|	15079	|	1	|	15121	|	5	|
|	15038	|	1	|	15080	|	1	|	15122	|	4	|
|	15039	|	4	|	15081	|	4	|	15123	|	1	|
|	15040	|	1	|	15082	|	2	|	15124	|	3	|
|	15041	|	1	|	15083	|	1	|	15125	|	1	|
|	15042	|	3	|	15084	|	1	|		-		| - |



#### Reportar Fallo. 
