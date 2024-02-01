from django.db import models
from accounts.models import Account

class ProductRequest(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    vendor = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='images/')
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'Product Requests'
        ordering = ['-date_created']

    
   



