# Generated by Django 4.1.3 on 2022-12-08 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_customuser_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
    ]