from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from posts.views import (
    PostViewSet,
    CommentViewSet,
    FollowViewSet,
    GroupViewSet
)

router = routers.DefaultRouter()
router.register(r"follow", FollowViewSet, basename='follow')
router.register(r"groups", GroupViewSet, basename='group')
router.register(r"posts", PostViewSet, basename='posts')
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("api/v1/jwt/create/",
         TokenObtainPairView.as_view(), name="token_create"
         ),
    path("api/v1/jwt/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"
         ),
    path("api/v1/jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
