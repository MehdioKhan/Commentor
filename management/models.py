from django.db import models
from .fields import DomainNameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Site(models.Model):
    domain = DomainNameField(blank=False,unique=True,verbose_name=_('Domain'))
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='sites',
                              verbose_name=_('Site Owner'))

    def __str__(self):
        return self.domain


class Configuration(models.Model):
    allow_anonymouse = models.BooleanField(verbose_name=_('Anonymouse Comments'),
                                           default=False)
    site = models.OneToOneField(to='Site',on_delete=models.CASCADE,
                                related_name='config')

    def __str__(self):
        return "{}'s configuration".format(self.site)


class ModerationSetting(models.Model):
    moderate_all = models.BooleanField(default=False,
                                       verbose_name=_('Require all comments to be '
                                                      'approved manually'))
    moderate_anonymouse = models.BooleanField(default=True,
                                              verbose_name='Require anonymous comments '
                                                           'to be approved manually')
    site = models.OneToOneField(to='Site',on_delete=models.CASCADE,
                                related_name='moderation')

    def __str__(self):
        return "{}'s moderation settings".format(self.site)
