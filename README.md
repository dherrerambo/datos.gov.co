# datos.gov.co
Consumir datos abiertos de www.datos.gov.co

# uso
Se debe instalar la librería sodapy
~~~python
pip install sodapy
~~~

El inventario se obtiene en forma de Diccionario, asi:
~~~python
inventory = get_inventory()  # dict: {id: metadata}
~~~

Para convertir en DataFrame podemos usar:
~~~python
import pandas as pd
from datos_abiertos import get_inventory

i_datos = get_inventory()
df_i = pd.DataFrame.from_dict(i_datos, orient='index')
df_i.head()
~~~
