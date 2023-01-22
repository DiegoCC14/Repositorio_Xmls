from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class XmlModel( models.Model ):
	id = models.AutoField( primary_key=True )
	id_user = models.ForeignKey( User , on_delete=models.CASCADE )
	description = models.CharField( max_length=900 )
	fecha = models.DateTimeField( default=datetime.now( tz=timezone.utc ) )
	file_xml = models.FileField( upload_to='app/static/xml' )
	image_xml = models.ImageField( default='app/static/img/image_xml.webp' , blank=True )
	url = models.CharField( max_length=200 )

	def __str__(self):
		return str( self.id ) + " - " + str( self.file_xml )
