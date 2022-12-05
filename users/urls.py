from django.urls import include, path, re_path
from users import views
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")

urlpatterns = [
    re_path(r"^users/me/$", views.CurrentUser.as_view(), name="current-user"),
    path("", include(router.urls)),
    path(
        "users/<int:pk>/statistics/",
        views.UserStatistics.as_view(),
        name="user-statistics",
    ),
]
