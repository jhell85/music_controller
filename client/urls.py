from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('join', views.index),
    path('create', views.index),
    path('create/', views.index), # This is here because Chrome kept tacking a / at the end of the route causing it to break while developing
    path('room/<str:roomCode>',views.index)
]