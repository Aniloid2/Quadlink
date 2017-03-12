from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from authentication.models import HumanUser, MyUser

# Create your views here.


def registeruser(request):
	if request.method == "GET":
		print ('got request to send usernform')
		return render(request, 'registeruser/registeruser.html')

	if request.method == "POST":
		print ('got data back')
		username = request.POST.get('username')
		password = request.POST.get('password')
		type_user = 'human'

		print (username, password)

		auth_user = authenticate(username = username,password = password)
		if auth_user:
			print (' you already have an account')
			return HttpResponseRedirect('/login')
		else:
			print ('creating account')
			try :
				user = MyUser.objects.create_user(username = username, type_user = type_user , password = password)
				print ('MyUser has been created')
			except Exception as e:
				print (e)

			
			try:
				HumanUser.objects.create(user = user)
				print ('Human user created')
			except Exception as e:
				print (e)


			Human_from_backend = MyUser.objects.get(username = username)
			print ('first name retrived', Human_from_backend.id)

			return HttpResponseRedirect('/login')

		
