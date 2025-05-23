from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/pair/', views.PairLookupView.as_view(), name='pair_lookup'),
]
