# Generated by Django 2.1 on 2018-10-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_auto_20181003_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='items_type',
            field=models.CharField(choices=[('Blouse', 'Blouse'), ('Shirts', 'Shirt'), ('Skirts', 'Skirt'), ('Gown', 'Gown')], default='Skirts', max_length=6),
        ),
    ]
