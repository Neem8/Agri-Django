# Generated by Django 5.0.1 on 2024-01-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=30)),
                ('farmer_email', models.EmailField(max_length=200, unique=True)),
                ('farmer_phone', models.CharField(max_length=200)),
                ('farmer_address', models.CharField(max_length=2000)),
                ('farmer_password', models.CharField(max_length=200)),
            ],
        ),
    ]
