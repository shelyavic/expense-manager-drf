from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from users.serializers import UserSerializer, UserStatisticsSerializer
from users.models import CustomUser
from users.permissions import IsOwner
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

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwner | IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = serializer.save()
        for category_name in DEFAULT_CATEGORIES:
            category, is_created = Category.objects.get_or_create(name=category_name)
            category.users.add(user)


class UserStatistics(RetrieveAPIView):
    queryset = CustomUser.objects.prefetch_related("transaction_set")
    serializer_class = UserStatisticsSerializer
    permission_classes = [IsOwner | IsAdminUser]


class CurrentUser(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
