from django.contrib.auth.backends import ModelBackend
from authentication.models import MyUser

class AppUserAuth(ModelBackend):
	def authenticate(self, username, password):
		print ('authenticating....')
		try :
			user =  MyUser.objects.get(username= username)
			Password_pass = user.check_password()
			print ('is password_pass?', Password_pass)
			if Password_pass == True:
				return user 
		except Exception as e:
			print (e)
			return None