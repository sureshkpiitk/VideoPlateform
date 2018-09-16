import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models
from djchoices import ChoiceItem
from djchoices import DjangoChoices


class VideoTypeChoices(DjangoChoices):
    funny = ChoiceItem(value='FUNNY', label=_("funny"))
    comedy = ChoiceItem(value='C', label=_("comedy"))


class VideoType(models.Model):
    video_type = models.CharField(max_length=10, choices=VideoTypeChoices.choices, null=True, blank=True, db_index=True)

    class Meta:
        app_label = 'video'


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    video = models.FileField()
    created_on = models.DateTimeField(auto_created=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    likes = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    subscribed = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey('authentication.User', related_name='videos', db_index=True, on_delete=models.PROTECT)
    type = models.ManyToManyField('video.VideoType', blank=True, db_index=True)
    deleted_on = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey('authentication.User', null=True, blank=True, default=None, related_name='video_delete_user',
                                   on_delete=models.DO_NOTHING, db_index=False)
    video_played = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'video'


class PlayList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.ManyToManyField('video.Video', blank=True, db_index=True, related_name='playlist')
    created_by = models.ForeignKey('authentication.User', null=True, blank=True, default=None, related_name='playlist_created_by',
                                   on_delete=models.PROTECT, db_index=True)
    created_on = models.DateTimeField(auto_created=True)
    modified_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'video'
