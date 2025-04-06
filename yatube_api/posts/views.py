from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment, Follow
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = PageNumberPagination


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    pagination_class = PageNumberPagination
