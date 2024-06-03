from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.utils import timezone
from auth_app.models import CustomUser
from auth_app.filters import CustomUserFilter
from .models import UploadedFile

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        state = request.POST.get('state')
        birth_year = request.POST.get('birth_year')
        public_visibility = request.POST.get('public_visibility')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:
                user = CustomUser.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password, 
                    full_name=full_name, 
                    gender=gender, 
                    city=city, 
                    state=state,
                    birth_year=birth_year,
                    public_visibility=public_visibility
                )
                messages.success(request, 'Your account has been created. You can now log in.')
                return redirect('login')
    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember', None)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Browser close
            return redirect('authors_and_sellers')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'auth/login.html')

def authors_and_sellers_view(request):
    user_filter = CustomUserFilter(request.GET, queryset=CustomUser.objects.filter(public_visibility=True))
    return render(request, 'auth/authors_and_sellers.html', {'filter': user_filter})

def upload_file_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        visibility = request.POST.get('visibility') == 'on'
        cost = request.POST.get('cost')
        year_published = request.POST.get('year_published')
        file = request.FILES.get('file')

        if file and file.name.split('.')[-1].lower() in ['pdf', 'jpeg', ]:
            uploaded_file = UploadedFile(
                user=request.user,
                title=title,
                description=description,
                visibility=visibility,
                cost=cost,
                year_published=year_published,
                file=file
            )
            uploaded_file.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('uploaded_files')
        else:
            messages.error(request, 'Invalid file format. Please upload a PDF or JPEG file.')

    return render(request, 'auth/upload_file.html')

def uploaded_files_view(request):
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'auth/uploaded_files.html', {'uploaded_files': uploaded_files})

