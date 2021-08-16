# datos.gov.co
Consumir datos abiertos de www.datos.gov.co

# uso
Se debe instalar la librería sodapy
~~~python
pip install sodapy
~~~

El inventario se obtiene en forma de Dataframe, asi:
~~~python
inventory = get_inventory()  # dict: {id: metadata}
~~~
