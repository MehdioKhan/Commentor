from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserSingInSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(label=_("Password"),
                                     style={'input_type':'password'},
                                     trim_whitespace=False)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email')