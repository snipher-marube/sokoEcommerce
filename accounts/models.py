from django.db import models
from django.contrib.auth.models import AbstractUser


    
class Account(AbstractUser):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True) # unique=True means that no two users can have the same username
    email = models.EmailField(unique=True) # unique=True means that no two users can have the same email address
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    is_vendor = models.BooleanField(default=False)
    
    
    #login field
    USERNAME_FIELD = 'email' # username field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # required when user is created
    
    def save(self, *args, **kwargs):
        if self.is_active and not self.is_vendor:
            self.is_vendor = True
        super().save(*args, **kwargs)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    #methods
    def __str__(self):
        return self.email
    
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='userprofile/', blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.first_name
    
    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"
    

