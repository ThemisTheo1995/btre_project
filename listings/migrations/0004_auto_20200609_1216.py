# Generated by Django 3.0.6 on 2020-06-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200609_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='geo_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='listing',
            name='geo_lon',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
