# Generated by Django 4.1.3 on 2022-12-02 17:31

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
