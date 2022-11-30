from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import CustomUser

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    