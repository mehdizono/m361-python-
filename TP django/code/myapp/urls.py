
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Page d'accueil
    path('counter', views.counter, name='counter'), # Page du résultat
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

