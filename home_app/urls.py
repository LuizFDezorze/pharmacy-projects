from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('store/', views.store, name="store"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('dologin/', views.dologin, name="dologin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logouts/', views.logouts, name="logouts"),


]
