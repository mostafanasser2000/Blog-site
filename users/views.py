from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('forum')
        
        form  = LoginForm()
        return render(request, 'users/login.html', {'form':form})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # authenticate verifies username and password. 
                                                                               # if the username and password ar valid it returns an istance of User or None 
            
            if user:
                login(request, user)  # function logs a user in. technically it creates a session id on the server and sends it back to web browser in form of cockie
                messages.success(request, f'{username.title()}, Welcome back!')
                return redirect('forum')
            
        # either form is not valid or user not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('forum')


def sign_up(request):
    
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            messages.success(request, 'You have been singed up successfully!')
            login(request, user)
            return redirect('forum')

        else:
            return render(request, 'users/register.html', {'form': form})

               
            
        