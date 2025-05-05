from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('generate-pdf/', views.generate_test_pdf, name='generate_pdf'),
]
