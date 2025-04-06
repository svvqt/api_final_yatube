from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from posts.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r"follow", FollowViewSet, basename='follow')
router.register(r"group", GroupViewSet, basename='group')
router.register(r"posts", PostViewSet, basename='posts')
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    #path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    #path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
