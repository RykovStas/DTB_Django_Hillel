from drf_posts.models import Comment, Post

from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'created_at', 'link', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='comment-detail')

    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'created_at', 'link']
