from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('main', views.main, name="main"),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]