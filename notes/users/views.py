from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created!")
            return redirect("note-home")
    else:
        
        form = UserRegisterForm()    
        
    return render(request, "users/register.html", {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("note-home")
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render(request = request, template_name="users/login.html", context={"login_form":form})