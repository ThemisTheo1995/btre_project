# Generated by Django 3.0.6 on 2020-06-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_for_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='is_to_rent',
            field=models.BooleanField(default=False),
        ),
    ]
