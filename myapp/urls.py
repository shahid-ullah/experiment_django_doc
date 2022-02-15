# myapp/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('format_data/', views.format_data, name='format_data'),
]
