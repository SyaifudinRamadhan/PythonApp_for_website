from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginSys

# Create your views here.

class loginForm(forms.Form):
	username = forms.CharField(label = "Username")
	pwd = forms.CharField(label = "Password", max_length=15)

def login(request):

	form = loginForm()
	context = {
		'form':form,
	}
	print(request.POST)

	if request.method == "POST":
		usrname = request.POST['username']
		pwd = request.POST['pwd']
		authen = authenticate(request, username = usrname, password = pwd)

		if authen != None:
			loginSys(request, authen)
			print(request.user, authen)
			return redirect('/')
		else :
			context = {
				'form':form,
				'Notif': 'Masukkan username dan password yang benar bro !!!'
			}
			print(request.user)
			return render(request, 'login.html', context) 

	return render(request, 'login.html', context) 