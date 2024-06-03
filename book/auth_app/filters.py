import django_filters
from auth_app.models import CustomUser

class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['username','full_name','email','city', 'state', 'gender','birth_year']