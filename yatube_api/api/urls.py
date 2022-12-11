from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register('comments', CommentViewSet, basename='comments')
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls), name='api-root'),
]
