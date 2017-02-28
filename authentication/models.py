from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):



	def create_user(self,username,type_user, password): 
		"""
		Creates and saves a User without password. Username is an integer given by the facebook api ID
		"""

		user = self.model(
		    #username_id=username_id,
		    username = username,
		    type_user = type_user,
		)
		user.set_password(password)

		user.save(using=self._db)
		return user




class MyUser(AbstractBaseUser):
	# username_id = models.BigIntegerField(
	# 	verbose_name='username_id',
	# 	primary_key = True,
	# )

	username = models.CharField(
		verbose_name = 'userame',
		max_length = 100,
		unique = True,
		)

	type_user = models.CharField(
		verbose_name = 'type',
		max_length = 100,
		)

	USERNAME_FIELD = 'username'


	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	class Meta:
		managed = True



	def get_username_id(self):
		# The user is identified by their username
		return self.username_id

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin


class HumanUser(models.Model):
	user = models.OneToOneField(
		MyUser,
		on_delete=models.CASCADE,
		)

class QuadUser(models.Model):
	user = models.OneToOneField(
		MyUser,
		on_delete=models.CASCADE,
		related_name = 'quad_profile'
		)

	x_axis = models.PositiveIntegerField(
		verbose_name = "x_axis",
		default = 0,
		editable = True,
		)

	y_axis = models.PositiveIntegerField(
		verbose_name = "y_axis",
		default = 0,
		editable = True,
		)

	z_axis = models.PositiveIntegerField(
		verbose_name = "z_axis",
		default = 0,
		editable = True,
		)

	def get_x_axis(self):
		print ('im here')
		return self.x_axis

	def get_y_axis(self):
		return self.y_axis

	def get_z_axis(self):
		return self.z_axis


	class Meta:
		managed = True

	






