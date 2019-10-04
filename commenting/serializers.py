from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','body','parent','commenter','score','approved','parent')


class CommentCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','body','domain','path','parent','commenter')
