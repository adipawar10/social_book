from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#User = get_user_model()
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    birth_year = models.IntegerField(blank=True, null=True)
    public_visibility = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email']

    