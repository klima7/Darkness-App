from django.urls import path

from .views import PairsList

urlpatterns = [
    path('pairs/', PairsList.as_view())
]
