from django.urls import include, path
from rest_framework_nested.routers import NestedSimpleRouter

from api import views
from users.urls import router as users_router

app_name = "api"
router = NestedSimpleRouter(users_router, "users", lookup="user")
router.register("categories", views.CategoryViewSet, basename="category")
router.register("transactions", views.TransactionViewSet, basename="transaction")

urlpatterns = router.urls
