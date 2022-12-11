from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField("Category", max_length=255, unique=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="categories",
        related_query_name="category",
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    money_amount = models.DecimalField(
        "Amount of money", max_digits=8, decimal_places=2
    )
    organisation = models.CharField("Organisation", max_length=255)
    description = models.CharField("Description", max_length=255, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        "Date and Time of the transaction creation", auto_now_add=True
    )

    datetime = models.DateTimeField("Date and Time of the transaction", default=now)

    def __str__(self):
        return self.description
