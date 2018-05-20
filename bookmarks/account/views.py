from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def user_login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd  = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			if user is not None:
				#This is an attribute of Django's User model
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disable Account')
			else:
				return HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form':form})