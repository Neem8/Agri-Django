# Generated by Django 5.0.1 on 2024-01-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0004_delete_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
