# Generated by Django 2.1 on 2018-10-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0019_auto_20181004_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, to='ecom.Products'),
        ),
    ]