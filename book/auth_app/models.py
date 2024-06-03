from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import FileExtensionValidator

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

class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_files')
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploaded_files/')
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    year_published = models.IntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    