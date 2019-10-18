from rest_framework import serializers
from .models import Site,Configuration,Moderation


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = ('id','domain','owner')


class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = '__all__'


class ModerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moderation
        fields = '__all__'
