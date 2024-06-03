from django.contrib import admin
from auth_app.models import CustomUser
from django.utils import timezone


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'birth_year', 'public_visibility', 'calculate_age']

    def calculate_age(self, obj):
        if obj.birth_year:
            return timezone.now().year - obj.birth_year
        return None
    calculate_age.short_description = 'Age'

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)