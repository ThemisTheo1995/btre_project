# Generated by Django 3.0.6 on 2020-06-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200609_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=65.5, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=65.0, max_digits=9),
            preserve_default=False,
        ),
    ]