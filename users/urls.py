from django.urls import include, path
from users import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', views.UserViewSet, basename='user')

# urlpatterns = router.urls