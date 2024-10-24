from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm  # Import the login form
from django.contrib.auth import authenticate, login
from django.contrib import messages



from  . forms import SignupForm

# Create your views here.
# app_name/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my app!")



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })



# app_name/views.py

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                return redirect('/')  # Redirect to homepage after successful login
            else:
                messages.error(request, 'Invalid username or password')  # Show error message
    else:
        form = LoginForm()

    return render(request, 'app_name/login.html', {'form': form})

