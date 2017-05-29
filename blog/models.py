# @Author: pingjun
# @Date:   2017-05-30T06:17:27+08:00
# @Last modified by:   pingjun
# @Last modified time: 2017-05-30T06:21:24+08:00



from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
