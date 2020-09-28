from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='TaskManager-home'), #основна сторінка
    path('about/', views.about, name='TaskManager-about'),
]
