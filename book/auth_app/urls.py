from django.urls import path
from . import views
from .views import fetch_custom_users
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('authors-and-sellers/', views.authors_and_sellers_view, name='authors_and_sellers'),
    path('upload-file/', views.upload_file_view, name='upload_file'),
    path('uploaded-files/', views.uploaded_files_view, name='uploaded_files'),
    path('fetch_custom_users/', fetch_custom_users, name='fetch_custom_users'),
    
]
