from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from . import admin
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import VideoConference


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html',{'success':"Registration Successful. Please Login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error':error_message})
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error': "Invalid Credentials. Please try again."})
    return render(request, 'login.html')

@login_required 
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')

@login_required
def meeting_view(request, room_id):
    conference = get_object_or_404(VideoConference, room_id=room_id)
    full_name = request.user.first_name + " " + request.user.last_name
    return render(request, "videocall.html", {
        "name": full_name,
        "room_id": room_id
    })

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('/dashboard')  # restrict access

    users = User.objects.all()
    rooms = VideoConference.objects.all()
    return render(request, 'adminpanel.html', {'users': users, 'rooms': rooms})

@csrf_exempt
@login_required
def delete_user(request, user_id):
    if request.method == "POST" and request.user.is_superuser:
        User.objects.filter(id=user_id).delete()
    return redirect('admin_panel')

