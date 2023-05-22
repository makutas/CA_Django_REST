from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'body', 'user', 'user_id', 'user_email', 'created_on']