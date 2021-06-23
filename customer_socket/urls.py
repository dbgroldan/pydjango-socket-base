from django.urls import path
from .views import indexView, roomView

urlpatterns = [
    path('', indexView, name='index'),
    path('customer/<str:room>/<str:user_id>', roomView, name='room')
]