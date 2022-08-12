# Generated by Django 4.0.6 on 2022-08-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_commerce_offers_commerce_large_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commerce',
            name='large',
            field=models.BooleanField(default=False, verbose_name='large'),
        ),
        migrations.AlterField(
            model_name='commerce',
            name='medium',
            field=models.BooleanField(default=False, verbose_name='medium'),
        ),
        migrations.AlterField(
            model_name='commerce',
            name='small',
            field=models.BooleanField(default=False, verbose_name='small'),
        ),
    ]
