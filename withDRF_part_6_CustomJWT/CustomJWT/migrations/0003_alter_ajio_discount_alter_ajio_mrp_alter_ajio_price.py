# Generated by Django 5.0.2 on 2024-03-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomJWT', '0002_ajio_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajio',
            name='Discount',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='ajio',
            name='MRP',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='ajio',
            name='Price',
            field=models.CharField(max_length=64),
        ),
    ]
