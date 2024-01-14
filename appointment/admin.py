from django.contrib import admin

from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    search_fields = ('name', 'description')
    

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'email', 'phone_number', 'date', 'time', 'completed')
    list_filter = ('completed', 'created', 'updated')
    search_fields = ('user', 'service', 'email', 'phone_number')
    list_editable = ('completed',)
