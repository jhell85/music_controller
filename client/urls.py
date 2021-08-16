from django.urls import path
from .views import index

app_name = 'client'

urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create', index),
    path('create/', index), # This is here because Chrome kept tacking a / at the end of the route causing it to break while developing
    path('room/<str:roomCode>', index)
]