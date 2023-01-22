from pathlib import Path
from datetime import datetime
import random , string , os , json
from wsgiref.util import FileWrapper

from .services.download_xml_service import save_XML , get_XML_to_url

from models.models import XmlModel

#from wsgiref.util import FileWrapper

from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse , HttpResponse
from django.core.files import File
from django.utils import timezone

BASE_DIR = Path(__file__).resolve().parent.parent

class Home( View ):

	def get( self , request ):
		return render( request , 'home.html')


class Descargar_XML( View ):

	def post( self , request ):
		
		data_post = request.POST.dict()

		xml_dicc = get_XML_to_url( data_post['url_xml'] )
		
		if xml_dicc['xml'] != 'Indefinido':
			
			name_xml = ''.join( random.choice( string.ascii_lowercase ) for i in range(10)) + '.xml'
			
			save_XML( xml_dicc['xml'] , BASE_DIR , name_xml )
			
			objXml = XmlModel( id_user=request.user ,
							description= "Sin Descripcion XML" ,
							url= data_post['url_xml']	)

			with open( BASE_DIR/name_xml , 'rb' ) as file_xml:
				objXml.file_xml = File( file_xml , name_xml )
				objXml.save()

			os.remove( BASE_DIR/name_xml )

		return JsonResponse( {} )

class Obtener_XML( View ):

	def get( self , request ):

		List_ObjXml= XmlModel.objects.filter( id_user=request.user )
		
		list_data_xml = []
		
		for ObjXML in List_ObjXml:
			data = {}
			data["id"] = ObjXML.id
			data["descripcion"] = ObjXML.description
			data["url"] = ObjXML.url
			data["fecha_creacion"] = ObjXML.fecha
			data["imagen_xml"] = ObjXML.image_xml.url

			list_data_xml.append( data )

		return JsonResponse( { "xml_user" : list_data_xml })


def descargar_xml_file( request , id_xml ):
	ObjXML= XmlModel.objects.filter( id=id_xml , id_user=request.user )
	file = FileWrapper( open( BASE_DIR/ObjXML[0].file_xml.name , 'rb') )
	response = HttpResponse(file, content_type='application/xml')
	response['Content-Disposition'] = f'attachment; filename={"xml_archivo"}'
	return response

def borrar_xml_file( request ):
	data_request = request.POST.dict()
	ObjXML = XmlModel.objects.filter( id=data_request['id_xml'] , id_user=request.user )
	ObjXML.delete()
	return JsonResponse( {})