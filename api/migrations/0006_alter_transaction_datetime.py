# Generated by Django 4.1.3 on 2022-12-08 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_transaction_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Date and Time of the transaction",
            ),
        ),
    ]
