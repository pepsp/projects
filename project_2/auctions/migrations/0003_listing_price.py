# Generated by Django 5.0.4 on 2024-04-14 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing_comment_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_price', to='auctions.bid'),
        ),
    ]
