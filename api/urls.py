from django.urls import path
from .views import RandomPairView

urlpatterns = [
    path('random-pair/', RandomPairView.as_view(), name='random-pair'),
] 