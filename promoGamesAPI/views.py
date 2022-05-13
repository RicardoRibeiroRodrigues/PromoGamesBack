from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Favorite
from .serializers import FavoriteSerializer

# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def api_favorite(request, deal_id):
    try:
        favorite = Favorite.objects.get(deal_id=deal_id)
    except Favorite.DoesNotExist:
        raise Http404()

    if request.method == "post":
        new_favorite_data = request.data
        favorite.deal_id = new_favorite_data["deal_id"]
        favorite.title = new_favorite_data["title"]
        favorite.saving = new_favorite_data["saving"]
        favorite.thumb = new_favorite_data["thumb"]
        favorite.store_id = new_favorite_data["store_id"]
        favorite.save()
    if request.method == "DELETE":
        favorite.delete()
        remaining = Favorite.objects.all()
        serialized_favorites = FavoriteSerializer(remaining, many=True)
        return Response(serialized_favorites.data)

    serialized_favorite = FavoriteSerializer(favorite)
    return Response(serialized_favorite.data)


@api_view(["GET", "POST"])
def api_favorites(request):
    try:
        favorites = Favorite.objects.all()
    except Favorite.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        # Features primarias: Listar jogos em desconto atualmente e favoritar.
        print("Entrou aqui")
        new_entry_data = request.data
        favorite = Favorite(
            deal_id=new_entry_data["deal_id"],
            title=new_entry_data["title"],
            saving=int(float(new_entry_data["saving"])),
            thumb=new_entry_data["thumb"],
            store_id=int(new_entry_data["store_id"]),
        )
        favorite.save()

    serialized_favorites = FavoriteSerializer(favorites, many=True)
    return Response(serialized_favorites.data)
