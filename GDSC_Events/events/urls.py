from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('home/', views.home, name='home'),
    path('register/<int:event_id>/', views.register, name='register'),
] 