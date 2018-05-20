from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #create user profile


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	book_id = models.IntegerField(null = True, blank=False)
	book_name = models.CharField(max_length = 100,null = True, blank=False)
	previous_balance = models.FloatField(null = True, blank=False)
	copies_printed = models.IntegerField(null = True, blank=False)
	total_copies = models.IntegerField(null = True, blank=False)
	specimen_issued = models.IntegerField(null = True, blank=False)
	copies_sold = models.IntegerField(null = True, blank=False)
	balance_stock = models.FloatField(null = True, blank=False)
	royalty_rate = models.FloatField(null = True, blank=False)
	royalty_amount = models.FloatField(null = True, blank=False) 

	#show username of users
	def __str__(self):
		return self.user.username

def create_profile(sender , **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User) #user = default django user