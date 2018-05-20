from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# just check the home page

@login_required
def home(request):
	numbers = [1,2,3,4,5,6]
	name = 'AMBER GAUTAM'
	args = {'myname' : name, 'numbers' : numbers}
	return render(request, 'account/home.html', args)
	 #dictionary object"""

#Register user 

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()


			return redirect('/account/login/')
	else:
		form = RegistrationForm
	args = {'form' : form}
	return render(request, 'account/reg_forms.html', args)

#view profile
@login_required
def profile(request):
	args = {'user' : request.user}
	return render(request, 'account/profile.html', args)
#edit profile
@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			"""
			subject = "Thank you"
			message = 'Your confirmation email'
			from_email = settings.EMAIL_HOST_USER
			to_list = [save_it.email]
			send_mail(subject, message, from_email, to_list, fail_silently = False)
			"""
			return redirect('/account/profile')
	else:
		#blank form
		form =EditProfileForm(instance = request.user)
		args = {'form' : form}
		return render(request, 'account/edit_profile.html', args)
#reset password from original password
@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,  form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change_password')
	else:
		#blank form
		form =PasswordChangeForm( user = request.user)
		
		args = {'form' : form}
		return render(request, 'account/change_password.html', args)

