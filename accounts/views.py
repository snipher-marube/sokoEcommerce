from django.shortcuts import render, redirect
from django.contrib import  messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Account

def registerUser(request):
    

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('register')

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = authenticate(email=email, password=password)
            if user is not None:
                
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
            
        except Account.DoesNotExist:
            messages.error(request, 'Account does not exist')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')
