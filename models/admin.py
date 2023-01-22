from django.contrib import admin

from models.models import XmlModel


@admin.register(XmlModel)
class XmlAdmin( admin.ModelAdmin ):
	list_display = ( 'id' , 'id_user' , 'description' , 'fecha' , 'file_xml' , 'url' )
	fields = ( 'id_user' , 'description' , 'file_xml' , 'url' )
