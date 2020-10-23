#### Documentacion del proyecto

##### Metodo de estratificación univarida Dalenius&Hodges
Este método radica en la
formación de estratos de forma que la varianza obtenida sea mínima en cada estrato y
máxima entre cada uno de ellos, es decir, tiene por objetivo formar estratos que en su 
interior sean lo más homogéneos posible, y lo más diferentes entre los diferentes estratos
creados.

Dado un conjunto de _n_ observaciones de una variable x = (x<sub>1</sub> , x<sub>2</sub> ...x<sub>n</sub> ), el procedimiento para formar h  estratos a partir de estas observaciones sería el siguiente:

1.	Ordenar las observaciones de manera ascendente.

2.	Agrupar x = (x<sub>1</sub> , x<sub>2</sub> ...x<sub>n</sub> ) en un número _J_ de clases, donde _J_ = min {h ∗ 10, n}.
 

3.	Calcular los límites para cada clase de la siguiente manera:

 
> lim inf C<sub>k</sub> = min {x<sub>(i)</sub>} + (k — 1) ∗ ( max{x<sub>(i)</sub>} — min {x<sub>(i)</sub>} ) / J
 

> lim sup C<sub>k</sub> = min {x<sub>(i)</sub>}+ (k) ∗ (max{x<sub>(i)</sub>} — min {x<sub>(i)</sub>}) / J
 

Los intervalos se tomarán abiertos por la izquierda y cerrados por la derecha, a excepción del primero que será cerrado por ambos lados.

4.	A partir de estos límites, obtener la frecuencia de observaciones en cada clase

> f<sub>i</sub>	_i_ ∈ {1, … , J}.

5.	Calcular la raíz cuadrada de frecuencia en cada clase.

6.	Acumular la raíz cuadrada de las frecuencias en cada clase 

![formula](https://github.com/Arturo-GoGa/IMAGENES/blob/main/1.PNG)

7.	Dividir la suma de la raíz cuadrada de las frecuencias por el número de estratos:

![formula](https://github.com/Arturo-GoGa/IMAGENES/blob/main/2.PNG)

8.	Los puntos de corte de cada estrato se tomarán sobre el acumulado de la raíz cuadrada de las frecuencias en cada clase de acuerdo a lo siguiente: Q, 2Q, … , (h — 1)Q. Si el valor de Q queda entre dos clases, se tomará como punto de corte aquella clase que presente la mínima distancia a _Q_. Los límites de los h estratos conformados serán aquellos correspondientes a los límites inferior y superior de las clases comprendidas en cada estrato.
