# Generated by Django 4.0.4 on 2022-05-14 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promoGamesAPI', '0002_favorite_id_alter_favorite_deal_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='saving',
            new_name='savings',
        ),
    ]