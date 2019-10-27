from rest_framework import serializers
from .models import Comment,Page
from management.models import Site


class SiteSerializer(serializers.Serializer):
    domain = serializers.CharField()


class PageSerializer(serializers.ModelSerializer):
    site = SiteSerializer()

    class Meta:
        model = Page
        fields = ('site','path')

    def create(self,validated_data):
        site = Site.objects.get(domain=validated_data['site']['domain'])
        p,created = Page.objects.get_or_create(
            site=site,
            path=validated_data['path'],
        )
        if created:
            p.save()
        return p


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','body','parent','commenter','score','approved')


class CommentCRUDSerializer(serializers.ModelSerializer):
    page = PageSerializer()

    class Meta:
        model = Comment
        fields = ('id','body','page','parent','commenter')

    def create(self, validated_data):
        p = PageSerializer(data=validated_data['page'])
        p.is_valid(raise_exception=True)
        p.save()
        c = Comment.objects.create(
            body=validated_data['body'],
            page=p.instance,
            parent=validated_data['parent'],
            commenter=validated_data['commenter'],
        )
        c.save()
        return c
