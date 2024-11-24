from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# anytime you go to a website, you are *requesting* that website
# request gets sent to backend, and then returned etc

# always a three-step process in django: you need a view, you need home.html, and you need URLs 

def home(request):
	# statement to check if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# authentication
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			messages.success(request, "Welcome!")
			return redirect('home')
		else:
			messages.success(request, "Login error; please try again.")
			return redirect('home')
	else:
		return render(request, 'home.html', {})

# def login_user(request):
#	pass
#	ayooo chat is this the cause of all my woes

def logout_user(request):
	logout(request)
	messages.success(request, "See you next time!")
	return redirect('home')

def register_user (request):
	return render(request, 'register.html', {})

# login_user and logout_user instead of simply login and logout to avoid conflicting w/ imports