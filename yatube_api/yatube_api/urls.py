from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from posts.views import PostViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/<int:pk>/comments', CommentViewSet)
router.register(r'follow', FollowViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

