import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt

# CONEXIÓN A LA BASE DE DATOS
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost", # ruta conexion 
            user="root", # usuario
            password="campusfp", # contraseña del usuario
            database="ENCUESTAS" # bbdd a conectarse
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"NO SE PUEDE CONECTAR A LA BBDD: {err}") # mensaje error
        return None

# FUNCIONES 
# CARGAR COMBOBOX SEXO
def cargar_sexo():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            cursor.execute("SELECT DISTINCT Sexo FROM ENCUESTA") # consulta al campo de la bbdd a mostrar
            sexo_mostrar = [str(row[0]) for row in cursor.fetchall()] # recorremos para mostrar
            combobox_sexo['values'] = sexo_mostrar # mostramos en el combobox los datos obtenidos
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f" NO SE PUEDEN CARGAR LOS VALORES DE SEXO: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# CARGAR COMBOBOX DIVERSIÓN DEPENDENCIA ALCOHOL
def cargar_DiversionDependenciaAlcohol():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            cursor.execute("SELECT DISTINCT DiversionDependenciaAlcohol FROM ENCUESTA")  # consulta al campo de la bbdd a mostrar
            DiversionDependenciaAlcohol_mostrar = [str(row[0]) for row in cursor.fetchall()] # recorremos para mostrar
            combobox_diversion_dependencia['values'] = DiversionDependenciaAlcohol_mostrar # mostramos en el combobox los datos obtenidos
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUEDEN CARGAR LOS VALORES DE DIVERSIÓN DEPENDENCIA ALCOHOL: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# CARGAR COMBOBOX PROBLEMAS DIGESTIVOS
def cargar_ProblemasDigestivos():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            cursor.execute("SELECT DISTINCT ProblemasDigestivos FROM ENCUESTA") # consulta al campo de la bbdd a mostrar
            ProblemasDigestivos_mostrar = [str(row[0]) for row in cursor.fetchall()] # recorremos para mostrar
            combobox_problemas_digestivos['values'] = ProblemasDigestivos_mostrar # mostramos en el combobox los datos obtenidos
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUEDEN CARGAR LOS VALORES DE PROBLEMAS DIGESTIVOS: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# CARGAR COMBOBOX TENSION ALTA
def cargar_TensionAlta():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            cursor.execute("SELECT DISTINCT TensionAlta FROM ENCUESTA")  # consulta al campo de la bbdd a mostrar
            TensionAlta_mostrar = [str(row[0]) for row in cursor.fetchall()] # recorremos para mostrar
            combobox_tension_alta['values'] = TensionAlta_mostrar # mostramos en el combobox los datos obtenidos
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUEDEN CARGAR LOS VALORES DE TENSION ALTA: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# CARGAR COMBOBOX DOLOR CABEZA
def cargar_DolorCabeza():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            cursor.execute("SELECT DISTINCT DolorCabeza FROM ENCUESTA") # consulta al campo de la bbdd a mostrar
            DolorCabeza_mostrar = [str(row[0]) for row in cursor.fetchall()] # recorremos para mostrar
            combobox_dolor_cabeza['values'] = DolorCabeza_mostrar # mostramos en el combobox los datos obtenidos
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUEDEN CARGAR LOS VALORES DE DOLOR CABEZA: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# FUNCIÓN CREAR ENCUESTA
def crear_encuesta():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    # almacenamos en una variable todos los datos que vamos a necesitar .get para que los coja del formulario
    edad = entry_edad.get()
    sexo = combobox_sexo.get() 
    bebidas_semana = entry_bebidas_semana.get()
    cervezas_semana = entry_cervezas_semana.get()
    bebidas_fin_semana = entry_bebidas_fin_semana.get()
    bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
    vinos_semana = entry_vinos_semana.get()
    perdidas_control = entry_perdidas_control.get()
    diversion_dependencia = combobox_diversion_dependencia.get()
    problemas_digestivos = combobox_problemas_digestivos.get()
    tension_alta = combobox_tension_alta.get()
    dolor_cabeza = combobox_dolor_cabeza.get()
    
    # comprobamos que los campos del formulario estan completos
    if not edad or not sexo or not bebidas_semana or not cervezas_semana or not bebidas_fin_semana or not bebidas_destiladas_semana or not vinos_semana or not perdidas_control or not diversion_dependencia or not problemas_digestivos or not tension_alta or not dolor_cabeza:
        messagebox.showwarning("Campos incompletos", "Compelta todos los campos") # mensaje de error
        return
    
    if conexion:
        cursor = conexion.cursor()  # inicializamos la conexion 
        try:
            # consulta con un insert a la bbdd 
            cursor.execute("INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia, problemas_digestivos, tension_alta, dolor_cabeza))
            conexion.commit() # pasamos los cambios a la bbdd
            messagebox.showinfo("✓","ENCUESTA GUARDADAS") # mensaje si se inserta correctamente 
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUDIERON INGRESAR LAS RESPUESTAS: {err}") # mensaje de error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()
            mostrar_encuesta() # actualizamos el treeview con las encuestas

# FUNCIÓN MOSTRAR ENCUESTA
def mostrar_encuesta():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            for persona in treeview.get_children(): # limpiamos el treeview
                treeview.delete(persona)
            cursor.execute("SELECT * FROM ENCUESTA") # ejecutamos la consulta select a la bbdd cogiendo todos los campos
            for respuestas in cursor.fetchall():
                treeview.insert("", tk.END, values=respuestas) # mostramos los datos obtenidos en el treeview
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUEDEN CARGAR LOS DATOS: {err}") # mensaje de error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# FUNCIÓN SELECCIONAR ENCUESTA
def seleccionar_encuesta(event):
    try:
        item = treeview.selection()[0]  # lista con los elementos seleccionados
        respuestas = treeview.item(item, "values") # obtenemos los valores 

        entry_cod.config(state=tk.NORMAL) # habilitamos el campo 
        entry_cod.delete(0, tk.END) # limpiamos el campo
        entry_cod.insert(tk.END, respuestas[0]) # rellenamos el campo
        entry_cod.config(state=tk.DISABLED) # lo deshabilitamos

        entry_edad.delete(0, tk.END) # limpiamos el campo
        entry_edad.insert(tk.END, respuestas[1]) # rellenamos el campo

        combobox_sexo.set(respuestas[2]) # asignamos los valores al combobox

        entry_bebidas_semana.delete(0, tk.END) # limpiamos el campo
        entry_bebidas_semana.insert(tk.END, respuestas[3]) # rellenamos el campo

        entry_cervezas_semana.delete(0, tk.END) # limpiamos el campo
        entry_cervezas_semana.insert(tk.END, respuestas[4]) # rellenamos el campo

        entry_bebidas_fin_semana.delete(0, tk.END) # limpiamos el campo
        entry_bebidas_fin_semana.insert(tk.END, respuestas[5]) # rellenamos el campo

        entry_bebidas_destiladas_semana.delete(0, tk.END) # limpiamos el campo
        entry_bebidas_destiladas_semana.insert(tk.END, respuestas[6]) # rellenamos el campo

        entry_vinos_semana.delete(0, tk.END) # limpiamos el campo
        entry_vinos_semana.insert(tk.END, respuestas[7]) # rellenamos el campo

        entry_perdidas_control.delete(0, tk.END) # limpiamos el campo
        entry_perdidas_control.insert(tk.END, respuestas[8]) # rellenamos el campo

        combobox_diversion_dependencia.set(respuestas[9]) # asignamos los valores al combobox
        
        combobox_problemas_digestivos.set(respuestas[10]) # asignamos los valores al combobox

        combobox_tension_alta.set(respuestas[11]) # asignamos los valores al combobox

        combobox_dolor_cabeza.set(respuestas[12]) # asignamos los valores al combobox
    except IndexError:
        pass

# FUNCIÓN ACTUALIZAR ENCUESTA
def actualizar_encuesta():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    # almacenamos en una variable todos los datos que vamos a necesitar .get para que los coja del formulario
    edad = entry_edad.get()
    cod = entry_cod.get()
    edad = entry_edad.get()
    sexo = combobox_sexo.get()
    bebidas_semana = entry_bebidas_semana.get()
    cervezas_semana = entry_cervezas_semana.get()
    bebidas_fin_semana = entry_bebidas_fin_semana.get()
    bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
    vinos_semana = entry_vinos_semana.get()
    perdidas_control = entry_perdidas_control.get()
    diversion_dependencia = combobox_diversion_dependencia.get()
    problemas_digestivos = combobox_problemas_digestivos.get()
    tension_alta = combobox_tension_alta.get()
    dolor_cabeza = combobox_dolor_cabeza.get()
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        try:
            # consulta con un update a la bbdd 
            cursor.execute("UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s",(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia, problemas_digestivos, tension_alta, dolor_cabeza, cod))
            conexion.commit()  # pasamos los cambios a la bbdd
            messagebox.showinfo("✓","RESPUESTAS ACTUALIZADAS") # mensaje si se actualiza correctamente 
            mostrar_encuesta() # actualizamos las respuestas en el treeview llamando a la funcion
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUDIERON ACTUALIZAR LAS RESPUESTAS: {err}") # mensaje de error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# FUNCIÓN ELIMINAR ENCUESTA
def eliminar_encuesta():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    # almacenamos en una variable todos los datos que vamos a necesitar .get para que los coja del formulario
    cod = entry_cod.get()
    edad = entry_edad.get()
    sexo = combobox_sexo.get() 
    bebidas_semana = entry_bebidas_semana.get()
    cervezas_semana = entry_cervezas_semana.get()
    bebidas_fin_semana = entry_bebidas_fin_semana.get()
    bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
    vinos_semana = entry_vinos_semana.get()
    perdidas_control = entry_perdidas_control.get()
    diversion_dependencia = combobox_diversion_dependencia.get()
    problemas_digestivos = combobox_problemas_digestivos.get()
    tension_alta = combobox_tension_alta.get()
    dolor_cabeza = combobox_dolor_cabeza.get()

    if not edad or not sexo or not bebidas_semana or not cervezas_semana or not bebidas_fin_semana or not bebidas_destiladas_semana or not vinos_semana or not perdidas_control or not diversion_dependencia or not problemas_digestivos or not tension_alta or not dolor_cabeza:
        messagebox.showwarning("ERROR", "DEBES DE COMPLETAR TODOS LOS CAMPOS")
        return
    
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que quieres eliminar esta encuesta?") # mensaje para hacer una confirmacion de eliminacion de usuario
        if confirmacion:
            try:
                # consulta con un delete a la bbdd 
                cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (cod,))
                conexion.commit() # pasamos los cambios a la bbdd
                messagebox.showinfo("✓", "ENCUESTA ELIMINADA") # mensaje si se elimina correctamente 
                mostrar_encuesta() # actualizamos las respuestas en el treeview llamando a la funcion
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"NO PUDO ELIMINAR LA ENCUESTA: {err}") # mensaje error
            finally:
                # cerramos conexion
                cursor.close()
                conexion.close()
        else:
            messagebox.showinfo("Cancelado", "ELIMINACIÓN CANCELADA") # mensaje cancelacion eliminacion encuesta

# FUNCIÓN LIMPIAR CAMPOS FORMULARIO
def limpiar_campos():
    entry_cod.config(state=tk.NORMAL)# habilitamos el campo para poder editarlo
    entry_cod.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_cod.config(state=tk.DISABLED) # lo volvemos a deshabilitar
    entry_edad.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    combobox_sexo.set("") # .set para reestablecer valores del combobox
    entry_bebidas_semana.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_cervezas_semana.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_bebidas_fin_semana.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_bebidas_destiladas_semana.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_vinos_semana.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    entry_perdidas_control.delete(0, tk.END) # .delete eliminar los datos del campo correspondiente en el formulario
    combobox_diversion_dependencia.set("") # .set para reestablecer valores del combobox
    combobox_problemas_digestivos.set("") # .set para reestablecer valores del combobox
    combobox_tension_alta.set("") # .set para reestablecer valores del combobox
    combobox_dolor_cabeza.set("") # .set para reestablecer valores del combobox

# FUNCIÓN FILTRAR DATOS ENCUESTAS
def filtrar_datos():
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    # almacenamos en una variable todos los datos que vamos a necesitar .get para que los coja del formulario
    idEncuesta=entry_cod.get()
    edad = entry_edad.get()
    sexo = combobox_sexo.get() 
    bebidas_semana = entry_bebidas_semana.get()
    cervezas_semana = entry_cervezas_semana.get()
    bebidas_fin_semana = entry_bebidas_fin_semana.get()
    bebidas_destiladas_semana = entry_bebidas_destiladas_semana.get()
    vinos_semana = entry_vinos_semana.get()
    perdidas_control = entry_perdidas_control.get()
    diversion_dependencia = combobox_diversion_dependencia.get()
    problemas_digestivos = combobox_problemas_digestivos.get()
    tension_alta = combobox_tension_alta.get()
    dolor_cabeza = combobox_dolor_cabeza.get()
    
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        datos_filtrados = [] # inicializamos una lista para almacenar los datos a filtrar seleccionados por el usuario
        # consulta con un select a la bbdd donde coincidan los campso que introduce el usuario en el formulario
        consulta = "SELECT * FROM ENCUESTA WHERE 1=1"
        if idEncuesta: # variable del campo a filtrar
            consulta += " AND idEncuesta = %s" # consulta a la bbdd
            datos_filtrados.append(idEncuesta) # lo añadimos a la lista
        if edad:  # variable del campo a filtrar
            consulta += " AND edad = %s" # consulta a la bbdd
            datos_filtrados.append(edad) # lo añadimos a la lista
        if sexo: # variable del campo a filtrar
            consulta += " AND Sexo = %s" # consulta a la bbdd
            datos_filtrados.append(sexo) # lo añadimos a la lista
        if bebidas_semana: # variable del campo a filtrar
            consulta += " AND BebidasSemana = %s" # consulta a la bbdd
            datos_filtrados.append(bebidas_semana) # lo añadimos a la lista
        if cervezas_semana: # variable del campo a filtrar
            consulta += " AND CervezasSemana = %s" # consulta a la bbdd
            datos_filtrados.append(cervezas_semana) # lo añadimos a la lista
        if bebidas_fin_semana: # variable del campo a filtrar
            consulta += " AND BebidasFinSemana = %s"  # consulta a la bbdd
            datos_filtrados.append(bebidas_fin_semana) # lo añadimos a la lista
        if bebidas_destiladas_semana: # variable del campo a filtrar
            consulta += " AND BebidasDestiladasSemana = %s" # consulta a la bbdd
            datos_filtrados.append(bebidas_destiladas_semana) # lo añadimos a la lista
        if vinos_semana: # variable del campo a filtrar
            consulta += " AND VinosSemana = %s" # consulta a la bbdd
            datos_filtrados.append(vinos_semana) # lo añadimos a la lista
        if perdidas_control: # variable del campo a filtrar
            consulta += " AND PerdidasControl = %s" # consulta a la bbdd
            datos_filtrados.append(perdidas_control) # lo añadimos a la lista
        if diversion_dependencia: # variable del campo a filtrar
            consulta += " AND DiversionDependenciaAlcohol = %s"  # consulta a la bbdd
            datos_filtrados.append(diversion_dependencia) # lo añadimos a la lista
        if problemas_digestivos: # variable del campo a filtrar
            consulta += " AND ProblemasDigestivos = %s"  # consulta a la bbdd
            datos_filtrados.append(problemas_digestivos) # lo añadimos a la lista
        if tension_alta: # variable del campo a filtrar
            consulta += " AND TensionAlta = %s" # consulta a la bbdd
            datos_filtrados.append(tension_alta) # lo añadimos a la lista
        if dolor_cabeza:  #variable del campo a filtrar
            consulta += " AND DolorCabeza = %s" # consulta a la bbdd
            datos_filtrados.append(dolor_cabeza) # lo añadimos a la lista

        try:
            cursor.execute(consulta, datos_filtrados) # ejecutamos la consulta
            resultados = cursor.fetchall() # obtenemos los resultados
            for row in treeview.get_children(): # limpiamos el treeview
                treeview.delete(row)
            for row in resultados: 
                treeview.insert("", "end", values=row) # insertamos los datos filtrados
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUDO FILTRAR LOS DATOS: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# FUNCIÓN EXPORTAR DATOS FILTRADOS A EXCEL
def exportar_excel():
    rows = [] # inicializamos una lista vacía para almacenar las filas a exportar
    for row in treeview.get_children():
        rows.append(treeview.item(row, 'values')) # obtenemos los valores del treeview
    
    if not rows:
        messagebox.showwarning("Sin Datos", "NO HAY DATOS PARA EXPORTAR") # mensaje si no hay datos
        return
    
    # definimos las columnas del excel
    columnas = ["ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"]
    data_frame = pd.DataFrame(rows, columns=columnas) # creamos un dataframe para guardar columnas y filas en el excel
    guardar_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")]) # se abre una ventana para seleccionar la ruta y nombre del excel
    if guardar_archivo:
        try:
            data_frame.to_excel(guardar_archivo, index=False, engine='openpyxl')  # exportamos el dataframe al excel
            messagebox.showinfo("Éxito", f"Datos exportados correctamente a la ruta: {guardar_archivo}") # mensaje si se ha exportado correctamente
        except Exception as e:
            messagebox.showerror("Error", f"NO SE PUDO EXPORTAR EL ARCHIVO {e}") # mensaje error

# FUNCIÓN GENERAR GRÁFICO
def generar_grafico():
    # cogemos los datos de los combobox
    tipo_grafico = combo_tipo_grafico.get()
    filtro = filtro_combo_grafico.get()
    
    if tipo_grafico == "Elige el tipo de gráfico" or filtro == "Elige el filtro":
        messagebox.showwarning("Selección inválida", "Selecciona un tipo de gráfico y un filtro") # comprobamos que se han seleccionado los campos
        return
    
    conexion = conectar_db() # le pasamos la conexion de la bbdd
    if conexion:
        cursor = conexion.cursor() # inicializamos la conexion 
        # consulta con un select con el filtro seleccionado a la bbdd 
        consulta = f"SELECT {filtro} FROM ENCUESTA WHERE 1=1" 
        grafico = [] # inicalizamos una lista
        try:
            cursor.execute(consulta, grafico) # ejecutamos la consulta
            resultados = cursor.fetchall() # obtenemos los resultados
            data_frame = pd.DataFrame(resultados, columns=[filtro]) # los guardamos en un data frame
            if tipo_grafico == "Barras": # si se ha seleccionado barras
                sns.countplot(data=data_frame, x=filtro) # escribimos los datos a mostrar en funcion del tipo de grafico
                plt.title(f'Gráfico de {filtro}') # titulo del gráfico
                plt.show() # mostramos el gráfico
            elif tipo_grafico == "Líneas":
                sns.lineplot(data=data_frame, x=data_frame.index, y=filtro) # escribimos los datos a mostrar en funcion del tipo de grafico
                plt.title(f'Gráfico de {filtro}') # titulo del gráfico
                plt.show() # mostramos el gráfico
            elif tipo_grafico == "Circular":
                data_frame[filtro].value_counts().plot.pie(autopct='%1.1f%%', startangle=90) # escribimos los datos a mostrar en funcion del tipo de grafico
                plt.title(f'Gráfico de {filtro}') # titulo del gráfico
                plt.show() #mostramos el gráfico
            else:
                messagebox.showwarning("Error", "SELECCIONA UN TIPO DE GRÁFICO") #mensaje de error si no se ha seleccionado un tipo de grafico
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"NO SE PUDO GENERAR EL GRÁFICO: {err}") # mensaje error
        finally:
            # cerramos conexion
            cursor.close()
            conexion.close()

# DISEÑO INTERFAZ
ventana = tk.Tk()
ventana.title("Gestión de Encuestas")

# ESTILOS VENTANA
ventana.config(bg="#E8DCCA")
ventana.option_add("*Font", "Arial 12")

# ETIQUETAS Y ENTRADAS
tk.Label(ventana, text="Código:", bg="#E8DCCA").grid(row=0, column=0, padx=5, pady=3, sticky="e")
entry_cod = tk.Entry(ventana, state=tk.DISABLED)
entry_cod.grid(row=0, column=1, padx=5, pady=3)

tk.Label(ventana, text="Edad:", bg="#E8DCCA").grid(row=1, column=0, padx=5, pady=3, sticky="e")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=5, pady=3)

tk.Label(ventana, text="Sexo:", bg="#E8DCCA").grid(row=2, column=0, padx=5, pady=3, sticky="e")
combobox_sexo = ttk.Combobox(ventana, state="readonly")
combobox_sexo.grid(row=2, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Bebidas por Semana:", bg="#E8DCCA").grid(row=3, column=0, padx=5, pady=3, sticky="e")
entry_bebidas_semana = tk.Entry(ventana)
entry_bebidas_semana.grid(row=3, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Cervezas por Semana:", bg="#E8DCCA").grid(row=4, column=0, padx=5, pady=3, sticky="e")
entry_cervezas_semana = tk.Entry(ventana)
entry_cervezas_semana.grid(row=4, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Bebidas Fin de Semana:", bg="#E8DCCA").grid(row=5, column=0, padx=5, pady=3, sticky="e")
entry_bebidas_fin_semana = tk.Entry(ventana)
entry_bebidas_fin_semana.grid(row=5, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Bebidas Destiladas por Semana:", bg="#E8DCCA").grid(row=6, column=0, padx=5, pady=3, sticky="e")
entry_bebidas_destiladas_semana = tk.Entry(ventana)
entry_bebidas_destiladas_semana.grid(row=6, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Vinos por Semana:", bg="#E8DCCA").grid(row=7, column=0, padx=5, pady=3, sticky="e")
entry_vinos_semana = tk.Entry(ventana)
entry_vinos_semana.grid(row=7, column=1, padx=5, pady=3)

tk.Label(ventana, text="Num Pérdidas de Control:", bg="#E8DCCA").grid(row=8, column=0, padx=5, pady=3, sticky="e")
entry_perdidas_control = tk.Entry(ventana)
entry_perdidas_control.grid(row=8, column=1, padx=5, pady=3)

tk.Label(ventana, text="Diversión Dependencia Alcohol:", bg="#E8DCCA").grid(row=9, column=0, padx=5, pady=3, sticky="e")
combobox_diversion_dependencia = ttk.Combobox(ventana, state="readonly")
combobox_diversion_dependencia.grid(row=9, column=1, padx=5, pady=3)

tk.Label(ventana, text="Problemas Digestivos:", bg="#E8DCCA").grid(row=10, column=0, padx=5, pady=3, sticky="e")
combobox_problemas_digestivos = ttk.Combobox(ventana, state="readonly")
combobox_problemas_digestivos.grid(row=10, column=1, padx=5, pady=3)

tk.Label(ventana, text="Tensión Alta:", bg="#E8DCCA").grid(row=11, column=0, padx=5, pady=3, sticky="e")
combobox_tension_alta = ttk.Combobox(ventana, state="readonly")
combobox_tension_alta.grid(row=11, column=1, padx=5, pady=3)

tk.Label(ventana, text="Dolor de Cabeza:", bg="#E8DCCA").grid(row=12, column=0, padx=5, pady=3, sticky="e")
combobox_dolor_cabeza = ttk.Combobox(ventana, state="readonly")
combobox_dolor_cabeza.grid(row=12, column=1, padx=5, pady=3)

# BOTONES
tk.Button(ventana, text="INGRESAR", command=crear_encuesta, bg="#D5BA98").grid(row=14, column=0, sticky="ew" ,padx=100, pady=3)
tk.Button(ventana, text="ACTUALIZAR", command=actualizar_encuesta, bg="#D5BA98").grid(row=14, column=1, sticky="ew",padx=100, pady=3)
tk.Button(ventana, text="ELIMINAR", command=eliminar_encuesta, bg="#D5BA98").grid(row=15, column=0, sticky="ew",padx=100, pady=3)
tk.Button(ventana, text="LIMPIAR", command=limpiar_campos, bg="#D5BA98").grid(row=15, column=1, sticky="ew",padx=100, pady=3)
tk.Button(ventana, text="FILTRAR", command=filtrar_datos, bg="#D5BA98").grid(row=16, column=0, sticky="ew",padx=100, pady=3)
tk.Button(ventana, text="EXPORTAR A EXCEL", command=exportar_excel, bg="#D5BA98").grid(row=16, column=1, sticky="ew",padx=100, pady=3)
combo_tipo_grafico = ttk.Combobox(ventana, values=["Barras", "Líneas", "Circular"])
combo_tipo_grafico.set( "Elige el tipo de gráfico")
combo_tipo_grafico.grid(row=17, column=0, padx=100, pady=10, sticky="ew")

filtro_combo_grafico = ttk.Combobox(ventana, values=["ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
filtro_combo_grafico.set( "Elige el filtro")
filtro_combo_grafico.grid(row=18, column=0, padx=100, pady=10, sticky="ew")

tk.Button(ventana, text="Generar Gráfico", command=generar_grafico, bg="#D5BA98").grid(row=17, column=1, padx=100, pady=10, sticky="ew")

# TREEVIEW PARA MOSTRAR LISTA DE CLIENTES 
treeview = ttk.Treeview(ventana, columns=("ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"), show="headings")
treeview.bind("<ButtonRelease-1>", seleccionar_encuesta)
treeview.grid(row=19, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)


# COLUMNAS TREEVIEW
treeview.heading("ID", text="ID")
treeview.heading("Edad", text="EDAD")
treeview.heading("Sexo", text="SEXO")
treeview.heading("BebidasSemana", text="NUM BEBIDAS SEMANA")
treeview.heading("CervezasSemana", text="NUM CERVEZAS SEMANA")
treeview.heading("BebidasFinSemana", text="NUM BEBIDAD FIN SEMANA")
treeview.heading("BebidasDestiladasSemana", text="NUM BEBIDAS DESTILADAS SEMANA ")
treeview.heading("VinosSemana", text="NUM VINOS SEMANA")
treeview.heading("PerdidasControl", text="NUM PERDIDAS CONTROL")
treeview.heading("DiversionDependenciaAlcohol", text="DIVERSION DEPENDENCIA ALCOHOL")
treeview.heading("ProblemasDigestivos", text="PROBLEMAS DIGESTIVOS")
treeview.heading("TensionAlta", text="TENSION ALTA")
treeview.heading("DolorCabeza", text="DOLOR CABEZA")

# ANCHO DE LAS COLUMNAS
for col in treeview["columns"]:
    treeview.column(col, width=100, anchor="center")

# AJUSTAR TREEVIEW ANCHO VENTANA
ventana.grid_rowconfigure(19, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# LLAMADA DE FUNCIONES
mostrar_encuesta()
cargar_sexo()
cargar_DiversionDependenciaAlcohol()
cargar_DolorCabeza()
cargar_ProblemasDigestivos()
cargar_TensionAlta()

# EJECUTAR VENTANA
ventana.mainloop()