from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import JsonResponse

from authentication.models import QuadUser, MyUser


def realtimeup(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			return render(request, "userUpdate/piramid.html")
		else:
			return HttpResponseRedirect('/login/')


