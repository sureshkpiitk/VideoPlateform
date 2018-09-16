import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models
from djchoices import ChoiceItem, DjangoChoices

from authentication.util import age_validator


class GenderChoices(DjangoChoices):
    male = ChoiceItem(value='M', label=_("Male"))
    female = ChoiceItem(value='F', label=_("Female"))


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=255, unique=True, db_index=False)
    mobile = models.CharField(max_length=64, null=True, blank=True, db_index=True)
    created_on = models.DateTimeField(auto_created=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=2, choices=GenderChoices.choices, blank=True, null=True,
                              validators=[GenderChoices.validator])
    date_of_birth = models.DateField(null=True, blank=True, validators=[age_validator])
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey('self', null=True, blank=True, default=None, related_name='deleted_users',
                                   on_delete=models.PROTECT, db_index=False)
