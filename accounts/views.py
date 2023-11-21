from django.shortcuts import render

def registerUser(request):
    return render(request, 'accounts/register.html')

def loginUser(request):
    return render(request, 'accounts/login.html')
