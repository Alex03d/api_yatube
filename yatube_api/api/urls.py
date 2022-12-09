#  Импортируйте в код всё необходимое
from rest_framework.routers import SimpleRouter, DefaultRouter

from django.urls import include, path

from .views import PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls), name='api-root'),
]
