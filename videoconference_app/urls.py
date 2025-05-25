from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/', views.join_room, name = 'join_room'),
    path('',views.index, name='index'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]