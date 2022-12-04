from django.urls import include, path
from users import views
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "users/<int:pk>/statistics/",
        views.UserStatistics.as_view(),
        name="user-statistics",
    ),
]
