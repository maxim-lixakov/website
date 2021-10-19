from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="react.html")),
    path('year/',views.year),
    path('register/', views.form),
    path('month/', views.month),
    path('day/', views.day),
    path('note/', views.note),
    path('users/', views.users),
    path('newnote/', views.new_note)
]
