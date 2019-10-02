from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from .fields import DomainNameField


User = get_user_model()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=timezone.now())
    updated = models.DateTimeField(auto_now=timezone.now())

    class Meta:
        abstract = True


class Comment(BaseModel):

    APROVED = True # @TODO : get this flag from settings file
    body = models.TextField(blank=False,default='')
    domain = DomainNameField(blank=True,null=True)
    path = models.CharField(max_length=1500,blank=True,null=False)
    score = models.IntegerField(default=0)
    approved = models.BooleanField(default=APROVED)
    commenter = models.ForeignKey(to=User,blank=True,null=True,on_delete=models.SET_NULL
                                  ,related_name='comments')
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s Comment on {}".format(self.commenter,self.domain)

    def clean(self):
        if self.parent:
            parent_domain = self.parent.domain
            parent_path = self.parent.path
            if parent_domain != self.domain:
                raise ValidationError('Entered domain and parent domain must be same')
            if parent_path != self.path:
                raise ValidationError('Entered path and parent path must be same')
            if self.parent.deleted:
                raise ValidationError("You can't use deleted comment as parent")
        super(Comment,self).clean()
