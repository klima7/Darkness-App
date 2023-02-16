from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lobby.urls')),
    path('', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('randomcards/', include('random_cards.urls')),
    path('board/', include('board.urls')),
    path('tables/', include('tables.urls')),
]
