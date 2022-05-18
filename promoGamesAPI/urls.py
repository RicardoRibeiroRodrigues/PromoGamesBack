from django.urls import path
from . import views


urlpatterns = [
    path("api/favorites", views.api_favorites),
]
