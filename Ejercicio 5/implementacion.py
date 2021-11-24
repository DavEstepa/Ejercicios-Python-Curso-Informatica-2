"""La utilidad de los arrays booleanos, y sus funciones asociadas, se mostrara
    a continuacion usando una base de datos que contiene"""
    
import pandas as pd
import numpy as np

DB = pd.read_excel("datos.xlsx")
print(DB.head())
"""
  condicion1 condicion2         T1  ...         T6         T7         T8
0         CN         NS  27.161620  ...  23.039829  13.030990  19.293941
1         CN         NS  25.273304  ...  26.835311  25.014038  25.311231
2         CN         NS  11.914377  ...  41.486149  51.777552  46.339988
3         CN         NS  20.249416  ...  36.946598  37.474906  32.160050
4         CN         NS  30.214290  ...  15.909904  14.862695   9.912868

[5 rows x 10 columns]

La base de datos que se tiene puede interpretarse como una serie de curvas realizadas
durante la ejecucion de un experimento. Este experimento evalua dos grupos: CN Y EX; y
a su vez cada curva esta interferida por una segunda condicion, que las vuelve a dividir
en NS y SS. Es posible separar cada grupo de condiciones
"""

DB_CNNS = DB.iloc[np.array((DB['condicion1']=='CN') & (DB['condicion2'] =='NS'))]
"""
   condicion1 condicion2         T1  ...         T6         T7         T8
0          CN         NS  27.161620  ...  23.039829  13.030990  19.293941
1          CN         NS  25.273304  ...  26.835311  25.014038  25.311231
2          CN         NS  11.914377  ...  41.486149  51.777552  46.339988
3          CN         NS  20.249416  ...  36.946598  37.474906  32.160050
4          CN         NS  30.214290  ...  15.909904  14.862695   9.912868
5          CN         NS  30.593583  ...  23.223008  25.193583  28.639070
6          CN         NS  28.899126  ...  15.828583  15.672795  14.625522
7          CN         NS  39.161320  ...  38.037543  34.435763  34.553911
8          CN         NS  14.211936  ...  11.346390  14.246204  10.174935
9          CN         NS  30.517769  ...  32.681052  25.914127  19.942078
10         CN         NS  29.788615  ...  40.421548  42.904827  37.424420
11         CN         NS  17.990555  ...  16.259902  13.953996  11.903934
12         CN         NS  25.051838  ...  10.094638  19.327839  19.957249

[13 rows x 10 columns]
"""
DB_CNSS = DB.iloc[np.array((DB['condicion1']=='CN') & (DB['condicion2'] =='SS'))]
"""
   condicion1 condicion2         T1  ...         T6         T7         T8
13         CN         SS  19.629761  ...  15.072114  26.916728  37.734200
14         CN         SS  19.849639  ...  12.160100  11.469195  12.189602
15         CN         SS  15.573817  ...  43.032833  37.887752  22.830934
16         CN         SS  20.054119  ...  36.026855  35.631299  18.718101
17         CN         SS  19.823953  ...  16.763564  15.266415  14.565028
18         CN         SS  17.805646  ...  26.598682  28.542941  23.641389
19         CN         SS  26.645651  ...  34.951569  33.962216  34.147366
20         CN         SS  23.556716  ...  33.436646  36.794693  24.160286
21         CN         SS   6.805017  ...  14.946128  16.716167  16.379980
22         CN         SS  13.109689  ...  20.963908  19.789556  14.051902
23         CN         SS  21.072873  ...  18.710074  15.386329  11.795100
24         CN         SS  15.089728  ...  14.175500  13.099033  11.970885
25         CN         SS  20.297441  ...  41.161229  26.483080  27.749592

[13 rows x 10 columns]
"""

""" -Lo anterior se podria repetir para acceder a las otras combinaciones de condiciones
    cambiando solo la condicion del array booleano.
    
    -la funcion iloc que se aplica sobre un DataFrame permite extraer datos de este
    basado en los indices. Por lo que al emplear esta funcion, el DataFrame que se 
    obtiene contiene las filas que se especifiquen dentro del [] y esto se puede acceder
    a la forma en que se accede a cualquier array (basados en enteros o con arrays booleanos).
"""

DB_T120 = DB.iloc[np.array((DB['T1']>=20))] #Extraer DataFrame donde todas las muestras T1 son mayores a 20
"""
   condicion1 condicion2         T1  ...         T6         T7         T8
0          CN         NS  27.161620  ...  23.039829  13.030990  19.293941
1          CN         NS  25.273304  ...  26.835311  25.014038  25.311231
3          CN         NS  20.249416  ...  36.946598  37.474906  32.160050
4          CN         NS  30.214290  ...  15.909904  14.862695   9.912868
5          CN         NS  30.593583  ...  23.223008  25.193583  28.639070
6          CN         NS  28.899126  ...  15.828583  15.672795  14.625522
7          CN         NS  39.161320  ...  38.037543  34.435763  34.553911
9          CN         NS  30.517769  ...  32.681052  25.914127  19.942078
10         CN         NS  29.788615  ...  40.421548  42.904827  37.424420
12         CN         NS  25.051838  ...  10.094638  19.327839  19.957249
16         CN         SS  20.054119  ...  36.026855  35.631299  18.718101
19         CN         SS  26.645651  ...  34.951569  33.962216  34.147366
20         CN         SS  23.556716  ...  33.436646  36.794693  24.160286
23         CN         SS  21.072873  ...  18.710074  15.386329  11.795100
25         CN         SS  20.297441  ...  41.161229  26.483080  27.749592
26         EX         NS  26.821853  ...  23.797078  24.738908  25.008044
28         EX         NS  21.003650  ...  23.205950  27.196120  26.116347
32         EX         NS  37.768588  ...  21.757883  29.022443  24.500030
33         EX         NS  25.980450  ...  38.623285  39.516443  39.820546
36         EX         NS  29.216263  ...  20.780589  23.818103  24.426929
38         EX         SS  23.064493  ...  31.077028  38.806923  26.922591
39         EX         SS  29.428548  ...  27.769533  22.919411  28.170649
40         EX         SS  38.171907  ...  58.105435  50.462810  46.929080
42         EX         SS  31.457403  ...  15.253606  14.216726  13.684230
43         EX         SS  25.430513  ...  24.053936  16.667057  15.724604
44         EX         SS  36.252251  ...  43.236047  47.736675  41.503724
45         EX         SS  23.025426  ...  17.620889  12.815691  13.388172
47         EX         SS  27.228480  ...  19.547512  16.911816  21.628258
48         EX         SS  26.612589  ...  34.362590  30.569623  21.884472
49         EX         SS  20.733693  ...  21.740429  19.096984  13.239003
50         EX         SS  26.945644  ...  46.992961  39.252754  27.288351

[31 rows x 10 columns]
"""
cantidad = np.sum(DB['T4'] >= 30) #DB es un DataFrame. Trabajar con este es como 
#un diccionario. Se accede a su contenido por medio del nombre de la columna, este
#retorna el contenido de la columna, el cual se evalua y su resulado es el array 
#booleano que se empleara para contar los elementos que cumplen con la condicion
print('La cantidad de curvas que presentan un nivel de T4 mayor a 30 son: ', cantidad)