from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Transaction, Category
from api.serializers import TransactionSerializer, CategorySerializer
from api.filtersets import TransactionFilterSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    @property
    def user_pk(self):
        return self.kwargs.get("user_pk")

    def get_queryset(self):
        if self.user_pk is None:
            return Category.objects.none()
        return get_object_or_404(get_user_model(), id=self.user_pk).categories.all()

    def perform_create(self, serializer):
        category, is_created = Category.objects.get_or_create(
            **serializer.validated_data
        )
        if not is_created and category.users.filter(pk=self.user_pk).exists():
            raise ValidationError({"name": "User already has this category"})
        category.users.add(self.user_pk)

    def perform_destroy(self, instance):
        instance.users.remove(self.user_pk)

    def perform_update(self, serializer):
        self.perform_destroy(serializer.instance)
        category, is_created = Category.objects.get_or_create(
            **serializer.validated_data
        )
        category.users.add(self.user_pk)


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransactionFilterSet
    ordering_fields = ["money_amount", "datetime"]
    ordering = ["-datetime"]

    @property
    def user_pk(self):
        return self.kwargs.get("user_pk")

    def get_queryset(self):
        if self.user_pk is None:
            return Transaction.objects.none()

        return get_object_or_404(
            get_user_model(), id=self.user_pk
        ).transaction_set.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.user_pk)
