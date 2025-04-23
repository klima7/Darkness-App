from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('api/pair/', views.PairLookupView.as_view(), name='pair_lookup'),
] 