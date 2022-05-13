from django.db import models

# Create your models here.
class Favorite(models.Model):
    deal_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    saving = models.IntegerField()
    thumb = models.URLField(max_length=200)
    store_id = models.IntegerField()
