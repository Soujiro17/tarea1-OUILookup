# Qué es tarea1-OUILookup?

Es una herramienta basada en línea de comandos desarrollada en Python 3.x para consultar el fabricante de una tarjeta de red dada su dirección MAC o su IP.

# Autor

Herramienta desarrollada por:
Vicente Reyes Cáceres (vicente.reyes@alumnos.uv.cl)

# Como instalar:

Para una correcta ejecución del programa, se deben instalar todas las librerías necesarias adjuntadas en el archivo "requirements.txt". En caso de Windows, basta con ingresar a la carpeta tarea1-OUILookup desde la línea en la línea de comandos (cmd) y ejecutar lo siguiente:

``pip install -r requirements.txt``

# Como funciona:

OUILookup es una herramienta que está diseñada para entregar el nombre del fabricante de una tarjeta de red a través de una IP o MAC entregada por el usuario, la cuál es obtenida a través de parámetros por él mismo, o a través de una librería llamada "getmac" (en el caso de que se ingrese como parámetro la IP). La búsqueda de las "vendors" se realiza a través de un archivo llamado "vendorsDB.txt", el cual contiene datos actualizados al día sobre las vendedoras de tarjetas gráficas.

# Compatibilidad:

La herramienta fue desarrollada y testeada en el SO Windows 10.
