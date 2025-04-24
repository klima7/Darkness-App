from django.urls import path
from . import views

app_name = 'faces'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:character>/', views.index, name='index_with_character'),
]
