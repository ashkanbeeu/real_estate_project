from django.urls import path
from . import views


urlpatterns = [
  path('login/', views.login, name='accounts_login'),
  path('register/', views.register, name='accounts_register'),
  path('logout/', views.logout, name='accounts_logout'),
  path('dashboard/', views.dashboard, name='accounts_dashboard'),
]
