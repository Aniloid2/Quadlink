from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout


def Rlogout(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			print ('user is autenticated, loging him out')
			logout(request)
			return HttpResponseRedirect('/login/')
		else:
			print ('user is not autenticated')
			return HttpResponseRedirect('/login/')


