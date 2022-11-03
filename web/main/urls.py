from django.urls import path
from . import views

urlpatterns = [
    path('year/', views.year),
    path('register/', views.form),
    path('month/', views.month),
    path('day/', views.day),
    path('note/', views.note),
    path('users/', views.users),
    path('newnote/', views.new_note),
    path('api/', views.api)
]
