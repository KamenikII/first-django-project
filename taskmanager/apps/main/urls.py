from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homeless'),
    path('about', views.about, name='contacts'),
    path('create', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
]
