from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AppointmentForm

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your appointment has been booked!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment/appointment.html', {'form': form})


