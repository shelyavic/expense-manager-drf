# Generated by Django 4.1.3 on 2022-11-30 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="users",
            field=models.ManyToManyField(
                related_name="categories",
                related_query_name="category",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]