from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
# router.register('api/v1/comments', CommentViewSet, basename='comments')
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(router.urls), name='api-root'),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
