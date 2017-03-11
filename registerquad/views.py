from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from authentication.models import QuadUser, MyUser
# Create your views here.

import requests 
import json


def registerquad(request):
	if request.method == "GET":
		print ('got request to send quadform')
		return render(request, 'registerquad/registerquad.html')

	if request.method == "POST":

	

		
		print ('got data back')
		quadname = request.POST.get('quadname')
		password = request.POST.get('password')
		type_user = 'quad'


		URL = 'https://quadlink-c80dc.firebaseio.com/'+ quadname +'.json'

		print (URL)

		print (quadname, password)
		auth_user = authenticate(username = quadname,password = password)
		if auth_user:
			print (' you already have an account')
			return HttpResponseRedirect('/login')
		else:
			print ('creating account')
			try :
				user = MyUser.objects.create_user(username = quadname, type_user = type_user , password = password)
				pass
			except Exception as e:
				print (e)

			print ('MyUser has been created')
			try:
				quaduser = QuadUser.objects.create(user = user)
			except Exception as e:

				bad_request = '404 bad request, account ID already exist, please choose anotherone'
				contex = {'bad_request' : bad_request}
				return render(request, 'badrequests/404_response.html', contex)
				print (e)

			payload = {
				'pitch': quaduser.get_pitch(),
				'roll': quaduser.get_roll(),
				'yaw': quaduser.get_yaw(),
				'temp': quaduser.get_temp(),
				'x_acc':quaduser.get_acc_x(),
				'y_acc':quaduser.get_acc_y(),
				'z_acc':quaduser.get_acc_z()
			}

			print (payload)


			r = requests.put(URL, data=json.dumps(payload))


			Quad_from_backend = MyUser.objects.get(username = quadname)
			print ('Retrived user ID', Quad_from_backend.id)



			return HttpResponseRedirect('/login')
