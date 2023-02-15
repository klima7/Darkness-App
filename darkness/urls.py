from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('api/', include('api.urls')),
    path('flashcards/', include('flashcards.urls')),
]
