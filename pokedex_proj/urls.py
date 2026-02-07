from django.contrib import admin
# import include to access different apps urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pokemon/', include("pokemon_app.urls")),
    path('api/v1/moves/', include("move_app.urls")),
    path('api/v1/pokeballs/', include('pokeball_app.urls')),
    path('api/accounts/', include("accounts.urls"))
]
