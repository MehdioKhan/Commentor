from django.db.models import CharField
from .validators import domain_name_validator


class DomainField(CharField):
    description = 'Domain name field'
    default_validators = [domain_name_validator]

    def __init__(self,*args,**kwargs):
        kwargs['max_length'] = 72
        super(DomainField,self).__init__(*args,**kwargs)
