from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # create superuser
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True) # unique=True means that no two users can have the same username
    email = models.EmailField(unique=True) # unique=True means that no two users can have the same email address
    phone_number = models.CharField(max_length=15)
    
    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False) # admin user; non super-user
    is_active = models.BooleanField(default=True) # active user
    is_staff = models.BooleanField(default=False) # staff user non super-user
    is_superuser = models.BooleanField(default=False) # superuser
    
    #login field
    USERNAME_FIELD = 'email' # username field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # required when user is created
    
    objects = MyAccountManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    #methods
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='userprofile/', blank=True)
    city = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.first_name
    
    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"
    

