from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Follow, Group, Post, Comment, User


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    validators = [UniqueTogetherValidator(
        queryset=Follow.objects.all(),
        fields=['user', 'following'])]

    def validate(self, data):
        if self.context['request'].user != data.get('following'):
            return data
        raise serializers.ValidationError(
            'Нельзя подписаться на себя'
        )

    class Meta:
        fields = ('__all__')
        model = Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.ReadOnlyField(source="post_id")

    class Meta:
        fields = "__all__"
        model = Comment

    def create(self, validated_data):
        post = validated_data.get('post')
        author = validated_data.get('author')
        text = validated_data.get('text')

        # Создаем новый комментарий
        return Comment.objects.create(post=post, author=author, text=text)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group
