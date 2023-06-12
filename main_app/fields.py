from django.core.validators import RegexValidator
from django.db import models

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 17)
        kwargs.setdefault('unique', True)
        kwargs.setdefault(
            'validators',
            [RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )]
        )
        super().__init__(*args, **kwargs)

class CostField(models.DecimalField):
    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, int):
            return value / 100
        return value

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None:
            return value
        return int(value * 100)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value is not None and value < 0:
            raise models.ValidationError("Cost value cannot be negative.")