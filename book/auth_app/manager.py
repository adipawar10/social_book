from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, email, username, password = None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        email = self.normalize_email(email)
        user = self.model(email = email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
    def create_superuser(self, email, username, password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    objects = UserManager()  # Custom user manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']