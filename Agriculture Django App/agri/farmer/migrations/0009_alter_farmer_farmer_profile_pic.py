# Generated by Django 5.0.1 on 2024-02-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_alter_farmer_farmer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='farmer_profile_pic',
            field=models.FileField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]