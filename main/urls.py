from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.urls import router as users_router

router = DefaultRouter()
router.registry.extend(users_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('', include('api.urls')),
]