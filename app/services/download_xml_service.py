import requests , time


def get_XML_to_url( url ):
	#retorna url y codigo http
	# { xml:  , code_reponse:  }
	try:
		resp = requests.get( url )
		dicc = {"xml": resp.content , "code_response" : str( resp.status_code ) }
	except:
		dicc = {"xml":"Indefinido" , "code_response" : str( resp.status_code ) }
	return dicc


def save_XML( xml , ubicasion , name ):
	with open( f'{ubicasion}/{name}' , 'wb') as foutput:
		foutput.write( xml )


if __name__ == "__main__":
	
	'''
	with open( 'XML\\2022-12-21__08@18@38.xml' , 'r') as xml1:
		with open( 'XML\\2022-12-21__08@18@57.xml' , 'r') as xml2:
			print( son_xml_iguales( xml1 , xml2 ) )
	'''