# Generated by Django 4.1.7 on 2023-03-19 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_profile_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobpost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('jobposition', models.TextField()),
                ('joblocation', models.TextField()),
                ('jobtime', models.TextField()),
                ('jobsalary', models.TextField()),
                ('jobabout', models.TextField()),
                ('joblink', models.TextField()),
            ],
        ),
    ]
