from django.urls import path
from .import views

from django.contrib.auth import views as auth_view


urlpatterns = [
    path('signup/',views.sign_up, name='sign_up'),
    path('userProfile/',views.userProfile, name='userProfile'),
    path('login/',auth_view.LoginView.as_view(template_name='Accounts/login.html'),name= 'login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='Accounts/logout.html'),name= 'logout'),
] 