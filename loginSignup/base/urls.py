from django.urls import path, include
from .views import home, authView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]
