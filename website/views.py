from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import Record

# anytime you go to a website, you are *requesting* that website
# request gets sent to backend, and then returned etc

# always a three-step process in django: you need a view, you need home.html, and you need URLs 

def home(request):
	# calling database here
	records = Record.objects.all()

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
		return render(request, 'home.html', {'records':records})

# def login_user(request):
#	pass
#	ayooo chat is this the cause of all my woes

def logout_user(request):
	logout(request)
	messages.success(request, "See you next time!")
	return redirect('home')

def register_user (request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Registration successful. Welcome to the database!")
			return redirect('home')
		else:
			form = SignUpForm()
			messages.success(request, "Your form has errors. Review them before proceeding.")
			return render(request, 'register.html', {'form':form})
	else:
		return render(request, 'register.html', {})
	return render(request, 'register.html', {'form':form})

# login_user and logout_user instead of simply login and logout to avoid conflicting w/ imports

def hoa_oc(request, pk):
	if request.user.is_authenticated:
		# retrieve record
		hoa_oc = Record.objects.get(id=pk)
		return render(request, 'record.html', {'hoa_oc':hoa_oc})
	else:
		messages.success(request, "Please log in first before proceeding.")
		return redirect('home')

def delete_oc(request, pk):
	if request.user.is_authenticated:
		delete_oc = Record.objects.get(id=pk)
		delete_oc.delete()
		messages.success(request, "OC successfully deleted.")
		return redirect('home')
	else:
		messages.success(request, "Please log in first before proceeding.")
		return redirect('home')

def add_oc(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "OC successfully added!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Please log in first before proceeding.")
		return redirect('home')

def update_oc(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "OC successfully updated.")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Please log in first before proceeding.")
		return redirect('home')




