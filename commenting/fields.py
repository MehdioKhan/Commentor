from django.db.models import CharField
from .validators import domain_name_validator
import re


class DomainField(CharField):
    description = 'Domain name field'
    default_validators = [domain_name_validator]

    def __init__(self,*args,**kwargs):
        kwargs['max_length'] = 72
        super(DomainField,self).__init__(*args,**kwargs)

    def clean(self, value, model_instance):
        def check(val):
            pattern = re.compile(r"https?://(www\.)?")
            result = pattern.sub('', val).strip().strip('/')
            return result
        value = check(value)
        model_instance.domain = value
        return value