from django.urls import path

from .views import Login, Register, Profile, logout

urlpatterns = [
   path("login/", Login, name="login-page"),
   path("register/", Register, name="register-page"),
   path("profile/", Profile, name="profile-page"),
   path("logout/", logout, name="logout"),



]