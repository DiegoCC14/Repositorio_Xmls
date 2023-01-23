
from django.shortcuts import render , redirect
from django.views import View

from django.contrib.auth import authenticate, login, logout


class Login( View ):

	def get( self , request ):
		if request.user.is_authenticated:
			return redirect('home')
		return render( request , 'login.html' )

	def post( self , request ):
		data_request = request.POST.dict()
		user = authenticate( username=data_request["username"], password=data_request["password"])
		if user is not None:
			login(request, user)
			return redirect('home')

		return redirect('login')


class Logout( View ):

	def get(self , request):
		logout(request)
		return redirect('login')