# Generated by Django 3.0.6 on 2020-06-25 12:12

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_auto_20200624_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='hidden',
            field=mapbox_location_field.models.AddressAutoHiddenField(),
        ),
    ]
