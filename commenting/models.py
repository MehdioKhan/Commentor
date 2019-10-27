from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from management.models import Site

User = get_user_model()


class Page(models.Model):
    site = models.ForeignKey(to=Site,on_delete=models.SET_NULL,null=True,
                             verbose_name=_('Site'))
    path = models.CharField(max_length=700,blank=False)
    locked = models.BooleanField(default=False)

    def __str__(self):
        return '{}{}'.format(self.site,self.path)


class Comment(models.Model):
    body = models.TextField(blank=False,default='',verbose_name=_('Comment body'))
    page = models.ForeignKey(to='Page',null=True,on_delete=models.CASCADE,related_name='comments')
    score = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    commenter = models.ForeignKey(to=User,blank=True,null=True,on_delete=models.SET_NULL
                                  ,related_name='comments')
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}'s Comment on {}".format(self.commenter,self.page)

    def clean(self):
        if self.parent:
            if self.parent.page != self.page :
                raise ValidationError('Page and parent page must be same')
            if self.parent.deleted:
                raise ValidationError("You can't use deleted comment as parent")
        super(Comment,self).clean()
