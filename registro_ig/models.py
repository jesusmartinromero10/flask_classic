import sqlite3
from tkinter import INSERT
from unittest import result

from config import ORIGIN_DATA

def select_all():
    conn= sqlite3.connect(ORIGIN_DATA)#conectamos con la bade de datos
    cur = conn.cursor()#creamos el cursor
    result = cur.execute("SELECT id, date, concept, quantity from movements order by date;")#hacemos la consulta la ejecuta la execute

    filas = result.fetchall()#transforma los datos en una lista de tuplas
    columnas = result.description
    #mezclar filas y columnas para obtener lista de diccionarios
    resultado = []
    for fila in filas:  #esto hace el diccionario con los datos
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)
    
    '''''
    es lo mismo que arriba
    resultado = []
    for fila in filas:
        d= {}
        for posicion, campo in enumerate(columnas): te pone posicion 0 campo id, posicion 1, campo fecha.... es lo que hace enumerate
            d(campo[0])= fila[posicion]
        resultado.append(d)
    '''

    conn.close()#cerrar conexion cursor
    return resultado


def insert(registro):
    '''''
    INSERT INTO moviments (date, concep, quantity ) values(?,?,?)

    params: cur.execute("INSERT INTO movements(date, concept,quantity) values(?,?,?)",[2022-04-08, 'cumple', -80])

    '''
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    result = cur.execute("INSERT INTO moviments(date, concept, quantity) values(?, ?, ?)", registro)
    conn.commit()
    conn.close()
    
    