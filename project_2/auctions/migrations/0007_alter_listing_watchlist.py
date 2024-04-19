# Generated by Django 4.2.11 on 2024-04-19 18:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listing_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listing_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
