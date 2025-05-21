from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homeless'),
    path('about', views.about, name='contacts'),
    path('create', views.create, name='create'),
]
