# Generated by Django 4.0.4 on 2022-05-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('savings', models.IntegerField()),
                ('thumb', models.URLField()),
                ('store_id', models.IntegerField()),
            ],
        ),
    ]
