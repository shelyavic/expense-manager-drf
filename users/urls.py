from django.urls import include, path
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")

urlpatterns = router.urls
