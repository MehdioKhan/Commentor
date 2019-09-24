from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


def expires_in(token):
    """ Return left time"""
    elapsed_time = timezone.now() - token.created
    remaining_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - elapsed_time
    return remaining_time


def is_token_expired(token):
    """ Check if token expired """
    return expires_in(token) < timedelta(seconds=0)


def token_expire_handler(token):
    """ If token is expired, token will remove and regenerate """
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(token.user)
    return is_expired,token


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User is not active')

        is_expired, token = token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed('Token is expired')

        return (token.user,token)


