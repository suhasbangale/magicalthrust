# Generated by Django 4.1.7 on 2023-03-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_profile_equity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.TextField(blank=True),
        ),
    ]
