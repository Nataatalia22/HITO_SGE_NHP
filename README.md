# HITO_SGE_NHP
Este proyecto es una aplicación en Python para la gestión de encuestas que permite almacenar, manipular y analizar respuestas mediante una base de datos. Está diseñado para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de manera sencilla y generar informes útiles.

Estructura del Proyecto
Script de Base de Datos (crear_bbdd.py): Se encarga de crear y configurar la base de datos donde se almacenarán las respuestas de la encuesta. Este script debe ejecutarse inicialmente para establecer la base de datos.

Aplicación Principal (app_encuestas.py): Un programa completo que:

Permite la gestión de respuestas de las encuestas mediante un conjunto de operaciones CRUD.
Exporta los datos almacenados a un archivo Excel para un fácil análisis y uso externo.
Genera gráficos visuales para interpretar mejor los resultados y tendencias de las encuestas.
#Funcionalidades Clave
Operaciones CRUD:

Crear: Añadir nuevas respuestas.
Leer: Visualizar respuestas existentes.
Actualizar: Modificar respuestas previamente almacenadas.
Eliminar: Borrar respuestas innecesarias.
Exportación a Excel:

Los datos de la encuesta pueden ser exportados a un archivo Excel con un solo clic, facilitando su análisis o distribución.
Generación de Gráficos:

Visualización de los datos mediante gráficos (de barras, circulares, etc.) para análisis estadísticos y presentación clara de los resultados.
Ejecuta crear_bbdd.py para inicializar la base de datos.
Ejecuta app_encuestas.py para gestionar las respuestas y analizar los datos.
Este proyecto es ideal para aquellos que necesitan un sistema simple y efectivo para gestionar y analizar encuestas.

#Requisitos
Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

Python 3.7 o superior: Descargar e instalar Python
Bibliotecas de Python:
sqlite3: Incluida en la instalación estándar de Python, para gestionar la base de datos.
pandas: Para la exportación de datos a archivos Excel.
matplotlib: Para la generación de gráficos visuales.
Instalación de bibliotecas: Puedes instalar las bibliotecas necesarias ejecutando el siguiente comando:
