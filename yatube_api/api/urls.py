from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token),
    path('v1/', include(router.urls)),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/$',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments'
    ),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/$',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post-comment-detail'
    ),
]
