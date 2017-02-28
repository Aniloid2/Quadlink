from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.contrib.auth import authenticate, login, logout

# structure to call a related object throu request.user.related_name.(variabel or method)
# Create your views here.

def Rlogin(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			print ('getting specific user')




			if request.user.type_user == 'quad':
				print ('its a quad!')
				logout(request)
				newquad_account = 'Please register another quadcopter or view activity as a user'
				contex = {'create_account' : newquad_account}
				return render(request, 'authapp/loginauth.html', contex)
			if request.user.type_user == 'human':
				print ('its a human')
				return HttpResponseRedirect('/realtimeup')
		else:
			print ('getting login page')
			return render(request, 'authapp/loginauth.html')

	if request.method == "POST":
		print ('recived data from anonimus user')

		username = request.POST.get('username')
		password = request.POST.get('password')

		print (username, password)

		auth_user = authenticate(username = username, password = password)
		print ('ive tried to auth')

		if auth_user:
			print ('user exists')
			login(request, auth_user)
			print ('this user has been logged in')
			return HttpResponseRedirect("/login/")
		else:
			print ('this user needs account..')
			create_account = 'account not found, retipe your username/password or register a drone or user'
			contex = {'create_account' : create_account}
			return render(request, 'authapp/loginauth.html', contex)
