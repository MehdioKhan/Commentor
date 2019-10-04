from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import domain_name_validator
import re


class DomainNameField(models.CharField):
    description = _('Domain name field')
    empty_strings_allowed = False
    default_validators = [domain_name_validator, ]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 72)
        super(DomainNameField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        def convert(val):
            domain_name_validator(value)
            pattern = re.compile(r"https?://(www\.)?")
            result = pattern.sub('', val).strip().strip('/')
            return result
        if isinstance(value, str) or value is None:
            return convert(value)
        return convert(str(value))