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
        favorite.savings = new_favorite_data["savings"]
        favorite.thumb = new_favorite_data["thumb"]
        favorite.store_id = new_favorite_data["store_id"]
        favorite.save()
    serialized_favorite = FavoriteSerializer(favorite)
    return Response(serialized_favorite.data)


@api_view(["GET", "POST", "DELETE"])
def api_favorites(request):
    try:
        favorites = Favorite.objects.all()
    except Favorite.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        # Features primarias: Listar jogos em desconto atualmente e favoritar.
        new_entry_data = request.data
        if not Favorite.objects.filter(deal_id=new_entry_data["deal_id"]).exists():
            favorite = Favorite(
                deal_id=new_entry_data["deal_id"],
                title=new_entry_data["title"],
                savings=int(float(new_entry_data["savings"])),
                thumb=new_entry_data["thumb"],
                store_id=int(new_entry_data["store_id"]),
            )
            favorite.save()
    if request.method == "DELETE":
        deal_id = request.data["deal_id"]
        favorite = Favorite.objects.get(deal_id=deal_id)
        favorite.delete()

    serialized_favorites = FavoriteSerializer(favorites, many=True)
    return Response(serialized_favorites.data)
