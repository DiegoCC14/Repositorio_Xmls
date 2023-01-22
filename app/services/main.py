import db_sql_service , download_xml_service , os , time
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def main():
	
	#Configuracion ------------>>>>>>>>>>>>>>>>
	url = "https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl"
	url = "https://www.w3schools.com/xml/plant_catalog.xml"
	url = "https://www.w3schools.com/xml/simple.xml"
	dir_xml = BASE_DIR/'XML'
	dir_db = BASE_DIR/'XML_DB.db'
	segundos_espera = 15
	# ------------------------->>>>>>>>>>>>>>>>
	
	while True:

		conn = db_sql_service.abrir_connection( dir_db )
		
		list_ultimo_xml = db_sql_service.get_rows_table( conn , "Ultimo_XML_ingresado" )
		
		dicc_respuesta_xml = download_xml_service.get_XML_to_url( url )

		if dicc_respuesta_xml["code_response"][0] != '2': #Error code response != 200 - 299 que es OK
			print(f"~~>>Error { dicc_respuesta_xml['code_response'] }")
			dicc_log = {"code_response": dicc_respuesta_xml["code_response"] , "descripcion": 'Indefinido'}
			db_sql_service.inserta_log_en_table_XML( conn , dicc_log ) #Ingresamos Log

		else: #Es 200-299 todo OK

			if len( list_ultimo_xml ) == 0: #No tiene registro, guardamos directamente
				
				print(f"~~>>New XML")

				dicc_log = {"code_response": dicc_respuesta_xml["code_response"] , "descripcion": 'Indefinido'}
				db_sql_service.inserta_log_en_table_XML( conn , dicc_log ) #Ingresamos Log				

				name_file = str( datetime.now() ).replace(' ','__').replace(':','@')[0:20] + '.xml'
				download_xml_service.save_XML( dicc_respuesta_xml["xml"] , dir_xml , name_file ) #guardamos el file.xml en dir: XML

				dicc_xml = {"id_Log": 1 , "name": name_file , "dir_carpeta": dir_xml }
				db_sql_service.inserta_xml_en_table_XML( conn , dicc_xml )

			else:

				direccion_file = dir_xml/list_ultimo_xml[0][2]
				ultimo_xml_ingresado = download_xml_service.open_xml( direccion_file )
				
				# ------------->>>>>>>>>>>>>>>>>> Porcion usada para la comparacion de archivos
				download_xml_service.save_XML( dicc_respuesta_xml["xml"] , BASE_DIR , 'new_file.xml' ) #guardamos el file.xml en dir: XML
				new_file = download_xml_service.open_xml( BASE_DIR/'new_file.xml' )
				os.remove( BASE_DIR/'new_file.xml' ) #eliminamos el archivo borrador
				# ------------->>>>>>>>>>>>>>>>>>
				
				if not( download_xml_service.son_xml_iguales( new_file , ultimo_xml_ingresado ) ):
					
					print(f"~~>>New XML")

					# Nuevo archivo, lo guardamos
					name_file = str( datetime.now() ).replace(' ','__').replace(':','@')[0:20] + '.xml'
					download_xml_service.save_XML( dicc_respuesta_xml["xml"] , dir_xml , name_file ) #guardamos el file.xml en dir: XML
					
					dicc_log = {"code_response": dicc_respuesta_xml["code_response"] , "descripcion": 'OK'}
					db_sql_service.inserta_log_en_table_XML( conn , dicc_log )
					
					ultimo_log_ingresado = db_sql_service.get_rows_table( conn , 'Ultimo_Logs_XML_Ingresado' )

					dicc_xml = {"id_Log": ultimo_log_ingresado[0][0] , "name": name_file , "dir_carpeta": dir_xml }
					db_sql_service.inserta_xml_en_table_XML( conn , dicc_xml )

		db_sql_service.cerrar_conexion( conn )
		time.sleep( segundos_espera )
		print(f"Procesando...{ datetime.now() }")

main()