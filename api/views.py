from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.models import Transaction, Category
from api.serializers import TransactionSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    @property
    def user_pk(self):
        return self.kwargs.get("user_pk")

    def get_queryset(self):
        return get_object_or_404(get_user_model(), id=self.user_pk).categories.all()

    def perform_create(self, serializer):
        category, is_created = Category.objects.get_or_create(
            **serializer.validated_data
        )
        if not is_created and category.users.filter(pk=self.user_pk).exists():
            raise ValidationError(
                    {"name": "User already has this category"}
                )
        category.users.add(get_user_model().objects.get(pk=self.user_pk))

    def perform_destroy(self, instance):
        instance.users.remove(get_user_model().objects.get(pk=self.user_pk))

    def perform_update(self, serializer):
        self.perform_destroy(serializer.instance)
        category, is_created = Category.objects.get_or_create(
            **serializer.validated_data
        )
        category.users.add(get_user_model().objects.get(pk=self.user_pk))


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        return get_object_or_404(get_user_model(), id=user_pk).transaction_set.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
