from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('service', 'email', 'phone_number', 'date', 'time', 'message')
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'service': 'Service',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'date': 'Date',
            'time': 'Time',
            'message': 'Message',
        }