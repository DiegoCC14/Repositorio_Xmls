import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def abrir_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect( db_file )
        return conn
    except Error as e:
        print(e)

def cerrar_conexion( conn ):
    conn.close()

def crea_tables_y_vistas( conn ):
    #El diagrama se encuentra en .Documentos/Diagrama_DB_XML.io
    #Creara en DB las sig. tablas y vistas:
        # table: XML
        # table: Logs_XML
        # view: XML_Reporte_Logs
        # view: Ultimo_XML_Ingresado
    
    c = conn.cursor()
    
    
    XML = f'CREATE TABLE XML( id INTEGER PRIMARY KEY AUTOINCREMENT , id_Log INT , name VARCHAR(500) , dir_carpeta VARCHAR(500) )'
    c.execute( XML )

    
    LOGS = f'CREATE TABLE Logs_XML( id INTEGER PRIMARY KEY AUTOINCREMENT , code_response VARCHAR(300) , descripcion VARCHAR(700) , fecha DATETIME DEFAULT CURRENT_TIMESTAMP )'
    c.execute( LOGS )
    
    
    VISTA_XML_Reporte_Logs = f'CREATE VIEW XML_Reporte_Logs AS '
    VISTA_XML_Reporte_Logs += f'SELECT code_response , COUNT(*) FROM Logs_XML GROUP BY code_response;'
    c.execute( VISTA_XML_Reporte_Logs )
    
    
    VISTA_Ultimo_XML_Ingresado = f'CREATE VIEW Ultimo_XML_Ingresado AS SELECT * FROM XML ORDER BY id DESC LIMIT 1 ;'
    c.execute( VISTA_Ultimo_XML_Ingresado )
    
    
    VISTA_Ultimo_Logs_XML_Ingresado = f'CREATE VIEW Ultimo_Logs_XML_Ingresado AS SELECT * FROM Logs_XML ORDER BY id DESC LIMIT 1 ;'
    c.execute( VISTA_Ultimo_Logs_XML_Ingresado )

    conn.commit()
    
def inserta_xml_en_table_XML( conn , dicc_xml ):
    #dicc_xml = {"id_Log":50 , "name": "archivo1" , "dir_carpeta":"c:buenas"}

    c = conn.cursor()

    #id es AUTO_INCREMENT
    COLUMNAS = ' id_Log , name , dir_carpeta '
    
    id_Log = dicc_xml["id_Log"]
    name = dicc_xml["name"]
    dir_carpeta = dicc_xml["dir_carpeta"]

    VALUES = f'{id_Log} , "{name}" , "{dir_carpeta}"'
    INSERT_ROW_XML = f'INSERT INTO XML({COLUMNAS}) VALUES ({VALUES})'
    c.execute( INSERT_ROW_XML )
    conn.commit()

def inserta_log_en_table_XML( conn , dicc_log ):
    #dicc_log = {"code_response": '200' , "descripcion": 'buenas gente como les va'}
    
    c = conn.cursor()

    #id es AUTO_INCREMENT
    COLUMNAS =  ' code_response , descripcion , fecha '
    COLUMNAS =  ' code_response , descripcion '
    
    code_response = dicc_log["code_response"]
    descripcion = dicc_log["descripcion"]

    VALUES = f'"{code_response}" , "{descripcion}" '
    INSERT_ROW_LOG_XML = f'INSERT INTO Logs_XML({COLUMNAS}) VALUES ({VALUES})'
    
    c.execute( INSERT_ROW_LOG_XML )

    conn.commit()

def get_rows_table( conn , name_table ):
    c = conn.cursor()
    c.execute( f"SELECT * FROM {name_table}")

    rows = c.fetchall()
    return [ row for row in rows ]

if __name__ == "__main__":
    dir_sqlite3 = BASE_DIR/'XML_DB.db'
    conn = abrir_connection( dir_sqlite3 )
    
    crea_tables_y_vistas( conn )
    
    '''
    dicc_xml = {"id_Log":50 , "name": "archivo1" , "dir_carpeta":"c:buenas"}
    inserta_xml_en_table_XML( conn , dicc_xml )
    

    dicc_log = {"code_response": '200' , "descripcion": 'buenas gente como les va'}
    inserta_log_en_table_XML( conn , dicc_log )
            
    print( get_rows_table( conn , 'XML' ) )
    print( get_rows_table( conn , 'Logs_XML' ) )
    print( get_rows_table( conn , 'Ultimo_XML_Ingresado' ) )
    print( get_rows_table( conn , 'XML_Reporte_Logs' ) )
    '''

    cerrar_conexion( conn )