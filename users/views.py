from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from users.serializers import UserSerializer, UserStatisticsSerializer
from users.models import CustomUser
from api.models import Category


DEFAULT_CATEGORIES = [
    "self care",
    "salary",
    "health and fitness",
    "cafes and restaurants",
    "car",
    "education",
    "recreation and entertainment",
    "payments, commissions",
    "purchases: clothes, appliances",
    "groceries",
    "travel",
]


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        for category_name in DEFAULT_CATEGORIES:
            category, is_created = Category.objects.get_or_create(name=category_name)
            category.users.add(user)


class UserStatistics(RetrieveAPIView):
    queryset = CustomUser.objects.prefetch_related("transaction_set")
    serializer_class = UserStatisticsSerializer
