# Generated by Django 3.0.6 on 2020-06-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0026_auto_20200627_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='property_type',
            field=models.CharField(choices=[('Bungalow', 'Bungalow'), ('Studio', 'Studio'), ('Land', 'Land'), ('Flat/Appartment', 'Flat/Appartment'), ('Commercial Property', 'Commercial Property'), ('House', 'House')], default='House', max_length=100),
        ),
    ]
