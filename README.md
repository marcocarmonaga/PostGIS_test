El presente documento es parte de un ejercicio acerca de carga de información en base de datos con CSV como input. 

Se anexa un archivo .sql el cual puede ser ejecutado dentro del motor de PosgreSQL, el requisito principal es tener instalado PostGIS como extensión a la base de datos. 

Además de este archivo .sql, también se anexan dos archivos .py, el archivo config.py únicamente tiene la función de generar la conexión con la base de datos, dicho archivo únicamente sirve como herramienta auxiliar al archivo main.py, el cual contiene la función principal en donde se desarrolla lo siguiente: 

- Si el nombre que se desea introducir ya existe, solamente debe actualizar la información restante. 

- Si la geometría que se desea introducir ya existe, no debe crearse ningún registro y el script debe reportar todo este tipo de incidencias en un archivo final que contenga un JSON a manera de log de errores. El JSON puede contener la estructura que se desee, simplemente que deje claro cuáles filas del CSV no pudieron cargarse debido a la duplicidad de geometrías. 

- Imprimir en pantalla un reporte final indicando: 

    - cuántos registros fueron creados, 

    - cuántos fueron actualizados (debido a que tenían el mismo nombre), 

    - cuántos fueron omitidos (debido a la duplicidad de geometrías). 

Dentro del script main.py se le pide al usuario indicar la dirección del archivo .csv a cargar, dentro de este repositorio se anexa un ejemplo para poder testear su funcionamiento, es por ello que al momento de que el script principal pida la dirección, bastará con poner `./data/test.csv` para realizar dicha prueba una vez ya haya sido cargada la base de datos y creada la tabla correspondiente. 

Finalmente, cabe mencionar que el archivo database.ini debe ser configurado de acuerdo con el propio sistema donde se vaya a hacer prueba alguna de la base de datos cargada en el archivo .sql 

NOTA: al momento de finalizar la carga de datos, es importante notar que las unidades de la columna área se encuentran calculadas en el esferoide determinado por el SRI, esto de acuerdo con [su misma documentación](https://postgis.net/docs/ST_Area.html). 