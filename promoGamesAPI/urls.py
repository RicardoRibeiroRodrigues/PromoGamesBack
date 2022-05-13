from django.urls import path
from . import views


urlpatterns = [
    path("api/favorites", views.api_favorites),
    path("api/favorites/<str:deal_id>/", views.api_favorite),
]
