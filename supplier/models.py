from django.db import models
from accounts.models import Account

class Commodity(models.Model):
    name = models.CharField(max_length=255)
    available_amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price per each commodity')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Commodities'
    
    def __str__(self):
        return self.name

class SupplyRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    supplier = models.ForeignKey(Account, on_delete=models.CASCADE)
    commodities = models.ManyToManyField(Commodity)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Supply Request'
        verbose_name_plural = 'Supply Requests'

    def __str__(self):
        return f"Supply Request #{self.pk} - {self.status}"
