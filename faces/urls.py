from django.urls import path
from . import views

app_name = 'faces'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/pair/', views.PairLookupView.as_view(), name='pair_lookup'),
]
