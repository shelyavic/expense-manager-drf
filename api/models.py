from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Category(models.Model):
    name = models.CharField(_("Category"), max_length=255, unique=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="categories",
        related_query_name="category",
    )


class Transaction(models.Model):
    money_amount = models.DecimalField(_("Amount of money"), decimal_places=2)
    organisation = models.CharField(_("Organisation"), max_length=255)
    description = models.CharField(_("Description"), max_length=255, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        _("Date and Time of the transaction"), auto_now_add=True
    )
