# Generated by Django 5.0.2 on 2024-03-15 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AJIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=255)),
                ('Price', models.CharField(max_length=255)),
                ('MRP', models.CharField(max_length=255)),
                ('Discount', models.CharField(max_length=255)),
                ('URL', models.CharField(max_length=255)),
            ],
        ),
    ]
