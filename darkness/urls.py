from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lobby.urls')),
    path('admin/', admin.site.urls),
    path('words/', include('words.urls')),
    path('board/', include('board.urls')),
    path('tables/', include('tables.urls')),
    path('letters/', include('letters.urls')),
    path('stories/', include('stories.urls')),
]
