from rest_framework import serializers
from .models import Post, Comment, PostLike, CommentLike


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    user_email = serializers.ReadOnlyField(source='user.email')
    post = serializers.ReadOnlyField(source='post.post_id')

    class Meta:
        model = Comment
        fields = ['comment_id', 'post', 'body', 'created_on', 'user', 'user_id', 'user_email']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    user_email = serializers.ReadOnlyField(source='user.email')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'post_id', 'title', 'body', 'user', 'user_id',
            'user_email', 'created_on', 'comments', 'comment_count', 'likes', 'image'
        ]

    def get_comment_count(self, post):
        return Comment.objects.filter(post=post).count()

    # Note: important to give a specific name to the method since it depends on the field name
    def get_likes(self, post):
        return PostLike.objects.filter(post=post).count()


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['postlike_id']
