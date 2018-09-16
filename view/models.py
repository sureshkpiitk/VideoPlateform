from django.db import models


class View(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.DO_NOTHING)
    video = models.ForeignKey('video.Video', on_delete=models.DO_NOTHING)
    play_on = models.DateTimeField(auto_now_add=True)
    total_play_time = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'view'
