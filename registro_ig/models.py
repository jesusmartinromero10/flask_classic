import sqlite3
from unittest import result



from config import ORIGIN_DATA

def select_all():
    conn= sqlite3.connect(ORIGIN_DATA)#conectamos con la bade de datos
    cur = conn.cursor()#creamos el cursor
    cur.execute("SELECT id, date, concept, quantity from movements order by date;")#hacemos la consulta la ejecuta la execute
    result = filas_to_diccionario(cur.fetchall(), cur.description)
    conn.close()
    return result

    ''''
    conn= sqlite3.connect(ORIGIN_DATA)#conectamos con la bade de datos
    cur = conn.cursor()#creamos el cursor
    cur.execute("SELECT id, date, concept, quantity from movements order by date;")#hacemos la consulta la ejecuta la execute

    filas = cur.fetchall()#transforma los datos en una lista de tuplas
    columnas = cur.description #te coge las columnas de esta forma (id,none,none,none)(date,none,nonenone)(concept,none,none..)
    #mezclar filas y columnas para obtener lista de diccionarios
    
    resultado = []
    valor_columnas = []
    for colum in columnas:
        
        valor_columnas.append(colum[0]) #cojo los titulos de las columnas
    for fila in filas:
        valores_completo = dict(zip(valor_columnas,fila)) #con el zip uno el titulo de la columna con el dato de la fila en el orden que aparecen
        resultado.append(valores_completo)
    
    conn.close()#cerrar conexion cursor
    return resultado
    '''
    '''''
    resultado = []
    for fila in filas:  #esto hace el diccionario con los datos
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)
    conn.close()#cerrar conexion cursor
    return resultado
    
    es lo mismo que arriba
    resultado = []
    for fila in filas:
        d= {}
        for posicion, campo in enumerate(columnas): te pone posicion 0 campo id, posicion 1, campo fecha.... es lo que hace enumerate
            d(campo[0])= fila[posicion]
        resultado.append(d)
    '''

    


def insert(registro):
    '''''
    INSERT INTO moviments (date, concep, quantity ) values(?,?,?)

    params: cur.execute("INSERT INTO movements(date, concept,quantity) values(?,?,?)",[2022-04-08, 'cumple', -80])

    '''
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    result = cur.execute("INSERT INTO movements (date, concept, quantity) values(?, ?, ?)", registro)
    conn.commit()
    conn.close()


def filas_to_diccionario(filas, columnas):

    resultado = []
    for fila in filas:  #esto hace el diccionario con los datos
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)
    
    return resultado

    '''
    lo mismo que lo de arriba
    resultado = []
    valor_columnas = []
    for colum in columnas:
        
        valor_columnas.append(colum[0]) #cojo los titulos de las columnas
    for fila in filas:
        valores_completo = dict(zip(valor_columnas,fila)) #con el zip uno el titulo de la columna con el dato de la fila en el orden que aparecen
        resultado.append(valores_completo)
    return resultado
    '''

def select_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("SELECT id, date, concept, quantity FROM movements where id = ?" , (id,))

    result = filas_to_diccionario(cur.fetchall(), cur.description)
    conn.close()

    if result:
        return result[0]
    else:
        return {}

    '''
    filas = result.fetchall()#transforma los datos en una lista de tuplas
    columnas = result.description #te coge las columnas de esta forma (id,none,none,none)(date,none,nonenone)(concept,none,none..)
    #mezclar filas y columnas para obtener lista de diccionarios
    
    
    
    conn.close()#cerrar conexion cursor
    return resultado
    '''

    '''
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("SELECT id, date, concept, quantity FROM movements where id = ?" , (id,))#tambien el id se puede poner [id]
    fila = cur.fetchone()#devuelve la fila si quieres jmuchas fetchall()
    conn.close()
    return fila
    '''

def delete_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("DELETE FROM movements where id = ?" , (id,))
    conn.commit()
    conn.close()
   
def modifica(registro):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("UPDATE movements  SET date = ? , concept = ?, quantity = ? where id = ?", registro)
    conn.commit()
    conn.close()
    