# datos.gov.co
Consumir datos abiertos de www.datos.gov.co
How to consume wwww.datos.gov.co

# uso/usage
Se debe instalar la librería [sodapy](https://github.com/xmunoz/sodapy)
Must install [sodapy](https://github.com/xmunoz/sodapy)
~~~python
pip install sodapy
~~~

El inventario se obtiene en forma de Diccionario, asi:
To fetch inventory as dictionary:
~~~python
inventory = get_inventory()  # dict: {id: metadata}
~~~

Para convertir en DataFrame podemos usar:
Make inventory as DataFrame:
~~~python
import pandas as pd
from datos_abiertos import get_inventory

i_datos = get_inventory()
df_i = pd.DataFrame.from_dict(i_datos, orient='index')
df_i.head()
~~~

Para obtener una tabla:
To get a report:
~~~python
from sodapy import Socrata

with Socrata("www.datos.gov.co", None) as client:
    response = client.get(id_of_report, limit=10)
    df = pd.DataFrame(response)

df.head()
~~~


