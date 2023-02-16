from django.urls import path
from . import views

app_name = 'random_cards'

urlpatterns = [
    path('', views.index, name='index')
]
