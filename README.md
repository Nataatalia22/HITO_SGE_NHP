# HITO_SGE_NHP
Este proyecto es una aplicación en Python diseñada para la gestión de encuestas. Permite almacenar, manipular y analizar las respuestas de las encuestas mediante una base de datos. Está orientada a realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de manera eficiente y a generar informes útiles para su análisis.

Estructura del Proyecto
1. Script de Base de Datos (crear_bbdd.py)
Este script es responsable de crear y configurar la base de datos donde se almacenarán las respuestas de la encuesta.
Debe ejecutarse inicialmente para establecer la base de datos antes de interactuar con la aplicación principal.
2. Aplicación Principal (app_encuestas.py)
Gestión de Respuestas: Permite realizar operaciones CRUD sobre las respuestas de la encuesta.
Exportación a Excel: Permite exportar los datos almacenados en la base de datos a un archivo Excel para facilitar su análisis y distribución.
Generación de Gráficos: Genera gráficos visuales (como gráficos de barras y circulares) para interpretar los resultados y observar las tendencias de las encuestas.
Funcionalidades Clave
1. Operaciones CRUD:
Crear: Añadir nuevas respuestas a la base de datos.
Leer: Visualizar respuestas existentes en la base de datos.
Actualizar: Modificar respuestas previamente almacenadas.
Eliminar: Eliminar respuestas innecesarias.
2. Exportación a Excel:
Los datos de las encuestas pueden ser fácilmente exportados a un archivo Excel con solo un clic, facilitando su análisis o distribución.
3. Generación de Gráficos:
La aplicación permite visualizar los datos de las encuestas mediante gráficos (de barras, circulares, etc.) para facilitar el análisis estadístico y la presentación de los resultados.
Instrucciones de Uso
Inicializar la Base de Datos:
Ejecuta el script crear_bbdd.py para inicializar la base de datos.

bash
Copiar código
python crear_bbdd.py
Gestionar Encuestas:
Ejecuta el script app_encuestas.py para gestionar las respuestas de las encuestas y analizar los datos.

bash
Copiar código
python app_encuestas.py
Este proyecto es ideal para aquellos que necesitan un sistema simple y efectivo para gestionar y analizar encuestas.

Requisitos
Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

Python 3.7 o superior:
Descargar e instalar Python

Bibliotecas de Python:

sqlite3: Incluida en la instalación estándar de Python, para gestionar la base de datos.
pandas: Para la exportación de datos a archivos Excel.
matplotlib: Para la generación de gráficos visuales.
Instalación de bibliotecas
Puedes instalar las bibliotecas necesarias ejecutando el siguiente comando:

bash
Copiar código
pip install pandas matplotlib
