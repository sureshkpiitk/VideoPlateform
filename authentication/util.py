from datetime import date

from django.core.exceptions import ValidationError


def age_validator(value):

    if value > date.today():
        raise ValidationError("Date of Birth can't be in future if you are not a time-traveller!")
