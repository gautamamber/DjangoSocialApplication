from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm

urlpatterns = [
	url(r'^$',views.home, name= 'home'),
	url(r'^login/$',login,{'template_name' : 'account/login.html'}),
	url(r'^logout/$',logout, {'template_name' : 'account/logout.html'}),
	url(r'^register/$',views.register, name = 'register'),
	#read data 
	url(r'^profile/$', views.profile, name = 'profile'),
	#edit
	url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
	#change password
	
	url(r'^change_password/$', views.change_password, name= 'change_password'),
	#reset password using email. use django builtin 
	url(r'^reset-password/$', password_reset, name = 'reset-password'),
	#it will show django reset password form 
	url(r'^reset-password/done/', password_reset_done, name = 'password_reset_done'),
	#Password reset confirm view
	#ISSUE
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(<?P<token>.+)/$', password_reset_confirm, name = 'password_reset_confirm'),
]
