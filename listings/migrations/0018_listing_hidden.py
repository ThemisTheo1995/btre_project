# Generated by Django 3.0.6 on 2020-06-24 20:54

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_auto_20200624_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='hidden',
            field=mapbox_location_field.models.AddressAutoHiddenField(default='Athens'),
        ),
    ]
